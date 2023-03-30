import datetime
import time
import threading
import paho.mqtt.client as mqtt
from gpiozero import LED, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from gtts import gTTS
import pygame
import json

class Patient:
    def __init__(self, check_in_time, led_pin, btn_pin, rpi_ip, name) -> None:
        self.check_in_time = check_in_time
        self.led_pin = led_pin
        self.btn_pin = btn_pin
        self.rpi_ip = rpi_ip
        self.patient_name = name
        self.init_mqtt()
        self.init_gpio()
        
    def start(self):
        # loop until it reaches the check in time
        while True:
            time.sleep(1)
            if datetime.datetime.now() > self.check_in_time:
                # notify user
                print('press button')

                # turn on led
                self.on_led()

                self.poll_thread = threading.Thread(target=self.poll_button)
                self.poll_thread.start()
                
                self.poll_thread.join()

    def poll_button(self):
        # start button poll
        self.btn.when_activated = self.on_button_press

        # start check in countdown timer
        self.check_in_timer_thread = threading.Timer(5, self.on_timer_end)
        self.check_in_timer_thread.start()

        # keep looping when btn is not press and still has a callback function
        while not self.btn.is_active and self.btn.when_activated:
            pass

    def on_button_press(self):
        # disable button
        self.btn.when_activated = None

        print('button pressed')
        self.check_in_timer_thread.cancel()
        self.off_led()

        payload = {"name":self.patient_name,
                   "cmd":"led_off"}

        self.mqtt_client.publish("to_hc_worker", json.dumps(payload))

        # set check in datetime for next day
        self.check_in_time = self.check_in_time + datetime.timedelta(days=1)

    def on_timer_end(self):
        # publish mqtt msg to HcWorker
        payload = {"name":self.patient_name,
                   "cmd":"led_on"}

        self.mqtt_client.publish("to_hc_worker", json.dumps(payload))
        print('mqtt msg published to HcWorker')

    def init_mqtt(self):
        broker = "test.mosquitto.org"
        port = 1883
        self.mqtt_client = mqtt.Client()  # create client object
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(broker, port)  # establish connection

        self.mqtt_client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        topic = self.patient_name.replace(' ','_')
        self.mqtt_client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        msg = json.loads(msg.payload)        
        if msg['cmd'] == 'led_off':
            self.off_led()
            # disable button
            self.btn.when_activated = None
            # set check in datetime for next day
            self.check_in_time = self.check_in_time + datetime.timedelta(days=1)
        
        elif msg['cmd'] == 'tts':
            self.play_sound_thread = threading.Thread(target=self.play_tts, args=(msg['lang'],msg['msg'],))
            self.play_sound_thread.start()
        
        elif msg['cmd'] == 'time':
            today = datetime.datetime.today()
            time = datetime.datetime.strptime(msg['time'], '%H:%M')
            self.check_in_time = datetime.datetime(today.year, today.month, today.day, time.hour, time.minute)
            print("New time set to: " + self.check_in_time)

    def init_gpio(self):
        if self.rpi_ip is None:
            self.led = LED(self.led_pin)
            self.btn = Button(self.btn_pin)
        else:
            factory = PiGPIOFactory(host=self.rpi_ip)
            self.led = LED(self.led_pin, pin_factory=factory)
            self.btn = Button(self.btn_pin, pin_factory=factory)

        print('gpio initialised')

    def on_led(self):
        self.led.on()
        print('led on')

    def off_led(self):
        self.led.off()
        print('led off')
    
    def play_tts(self, lang, msg):
        tts = None
        if lang == 'cn':
            tts = gTTS(text=msg, lang='zh-cn')
        else:
            tts = gTTS(text=msg, lang='en')
        tts.save("output.mp3")
        pygame.mixer.init()
        sound = pygame.mixer.Sound('./output.mp3')
        playing = sound.play()
        while playing.get_busy():
            pygame.time.delay(100)
