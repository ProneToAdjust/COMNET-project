import datetime
from Patient import Patient

LED_PIN = GPIO_PIN_NO
BTN_PIN = GPIO_PIN_NO
RPI_IP = 'RPI IP HERE'

# this will set the check in alert to sound 5 secs from initialisation
check_in_time = datetime.datetime.now()

pat = Patient(check_in_time, LED_PIN, BTN_PIN, RPI_IP)
pat.start()