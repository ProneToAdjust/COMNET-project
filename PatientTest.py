import datetime
from Patient import Patient

LED_PIN = 14
BTN_PIN = 15
RPI_IP = None
PATIENT_NAME = 'Sibei Suei'

# this will set the check in alert to sound 5 secs from initialisation
check_in_time = datetime.datetime.now()

pat = Patient(check_in_time, LED_PIN, BTN_PIN, RPI_IP, PATIENT_NAME)
pat.start()