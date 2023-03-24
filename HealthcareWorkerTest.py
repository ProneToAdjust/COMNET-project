from HealthcareWorker import HealthcareWorker

LED_PIN = GPIO_PIN_NO
BTN_PIN = GPIO_PIN_NO
RPI_IP = 'RPI IP HERE'

hc = HealthcareWorker(LED_PIN, BTN_PIN, RPI_IP)
hc.start()