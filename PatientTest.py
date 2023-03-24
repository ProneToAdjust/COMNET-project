import datetime
from Patient import Patient

LED_PIN = 2
BTN_PIN = 3
RPI_IP = None

# this will set the check in alert to sound 5 secs from initialisation
check_in_time = datetime.datetime.now()

pat = Patient(check_in_time, LED_PIN, BTN_PIN, RPI_IP)
pat.start()