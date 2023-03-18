import paho.mqtt.client as mqtt
from threading import Thread
from gpiozero import LED, Button
from gpiozero.pins.pigpio import PiGPIOFactory

class HealthcareWorker:
    def __init__(self, led_pin, btn_pin, rpi_ip) -> None:
        self.led_pin = led_pin
        self.btn_pin = btn_pin
        self.rpi_ip = rpi_ip
        self.init_mqtt()
        self.init_gpio()

    def start(self):
        while True:
            pass

    def poll_button(self):
        # start button poll
        self.btn.when_activated = self.on_button_press

        # keep looping when btn is not press and still has a callback function
        while not self.btn.is_active and self.btn.when_activated:
            pass

    def on_button_press(self):
            # disable button
            self.btn.when_activated = None

            self.led.off()
            self.client.publish('to_patient', 'off')

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
        msg = msg.payload.decode()
        
        if msg == 'on':
            self.led.on()
            print('led on')
            self.poll_thread = Thread(target=self.poll_button)
            self.poll_thread.start()

        elif msg == 'off':
            self.led.off()
            print('led off')

    def init_gpio(self):
        if self.rpi_ip is None:
            self.led = LED(self.led_pin)
            self.btn = Button(self.btn_pin)
        else:
            factory = PiGPIOFactory(host=self.rpi_ip)
            self.led = LED(self.led_pin, pin_factory=factory)
            self.btn = Button(self.btn_pin, pin_factory=factory)

        print('gpio initialised')