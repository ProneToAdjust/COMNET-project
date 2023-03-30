import datetime
from Patient import Patient

LED_PIN = GPIO_PIN_NO
BTN_PIN = GPIO_PIN_NO
RPI_IP = 'RPI IP HERE'
PATIENT_NAME = 'PATIENT NAME HERE'

# this will set the check in alert to sound 5 secs from initialisation
check_in_time = datetime.datetime.now()
check_out_time_limit = "00:00:20"

pat = Patient(check_in_time, check_out_time_limit, LED_PIN, BTN_PIN, RPI_IP, PATIENT_NAME)
pat.start()