import paho.mqtt.client as mqtt
from threading import Thread
from gpiozero import LED, Button
from gpiozero.pins.pigpio import PiGPIOFactory
import json

class HealthcareWorker:
    def __init__(self, led_pin, btn_pin, led_pin_2, btn_pin_2, rpi_ip) -> None:
        self.led_pin = led_pin
        self.btn_pin = btn_pin
        self.led_pin_2 = led_pin_2
        self.btn_pin_2 = btn_pin_2
        self.rpi_ip = rpi_ip
        self.init_mqtt()
        self.init_gpio()

    def start(self):
        while True:
            pass

    def poll_button(self, patient_name):
        # start button poll
        self.btn.when_activated = lambda : self.on_button_press(patient_name)

        # keep looping when btn is not press and still has a callback function
        while not self.btn.is_active and self.btn.when_activated:
            pass

    def poll_button_2(self, patient_name):
        # start button poll
        self.btn_2.when_activated = lambda : self.on_button_press_2(patient_name)

        # keep looping when btn is not press and still has a callback function
        while not self.btn_2.is_active and self.btn_2.when_activated:
            pass

    def on_button_press(self, patient_name):
            # disable button
            self.btn.when_activated = None

            self.led.off()
            topic = patient_name.replace(' ', '_')
            jsonString = json.dumps({"cmd": "led_off"})
            self.client.publish(topic, jsonString)

    def on_button_press_2(self, patient_name):
            # disable button
            self.btn_2.when_activated = None

            self.led_2.off()
            topic = patient_name.replace(' ', '_')
            jsonString = json.dumps({"cmd": "led_off"})
            self.client.publish(topic, jsonString)

    def init_mqtt(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect("test.mosquitto.org", 1883, 60)

        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe("to_hc_worker")

    def on_message(self, client, userdata, msg):
        msg = json.loads(msg.payload)
        
        if msg['cmd'] == 'led_on':
            if msg['name'] == 'Sibei Suei':
                self.led.on()
                print('led on')
                poll_thread = Thread(target=self.poll_button, args=(msg['name'],))
                poll_thread.start()
            elif msg['name'] == 'Sibei Sian':
                self.led_2.on()
                print('led_2 on')
                poll_thread = Thread(target=self.poll_button_2, args=(msg['name'],))
                poll_thread.start()

            
            print('led on')

        elif msg['cmd'] == 'led_off':
            if msg['name'] == 'Sibei Suei':
                self.led.off()
                print('led off')
            elif msg['name'] == 'Sibei Sian':
                self.led_2.off()
                print('led_2 off')
            

    def init_gpio(self):
        if self.rpi_ip is None:
            self.led = LED(self.led_pin)
            self.btn = Button(self.btn_pin)
            self.led_2 = LED(self.led_pin_2)
            self.btn_2 = Button(self.btn_pin_2)
        else:
            factory = PiGPIOFactory(host=self.rpi_ip)
            self.led = LED(self.led_pin, pin_factory=factory)
            self.btn = Button(self.btn_pin, pin_factory=factory)
            self.led_2 = LED(self.led_pin_2, pin_factory=factory)
            self.btn_2 = Button(self.btn_pin_2, pin_factory=factory)

        print('gpio initialised')
    
    def send_message(self, topic, msg):
        self.client.publish(topic, msg)