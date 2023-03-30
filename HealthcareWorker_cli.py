import os
from HealthcareWorker import HealthcareWorker
from threading import Thread
import json
from datetime import datetime
import time

hc = None
piThread = None

def editPatient():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
###############################################################
############## OPTION 1: EDIT PATIENT ALERT TIME ##############
############# SELECT A PATIENT TO EDIT ALERT TIME #############
###############################################################
0. Back to main menu""")
    patientFile = open("patients.txt", "r")
    count = 0
    patientList = []
    for name in patientFile:
        count += 1
        patientList.append(name)
        print("{count}. {name}".format(count=count, name=name).strip())
    patientFile.close()
    option = input("Enter your option: ")
    if option == '0':
        option()
    else:
        try:
            if int(option) <= count:
                changePatientTime(patientList[int(option)-1].replace(' ', '_').strip())
            else:
                editPatient()
        except:
            editPatient()
            
def changePatientTime(name):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
###############################################################
################## CHANGE PATIENT ALERT TIME ##################
###############################################################
0. Back to main menu""")
    timeStr = input("Enter new alert time (HH:MM): ")
    try:
        timeObject = datetime.strptime(timeStr, '%H:%M').time()
        jsonString = json.dumps({"cmd": "time", "time": timeStr})
        hc.send_message(name, jsonString)
        print("TIME CHANGED")
    except:
        changePatientTime(name)
    time.sleep(5)
    options()
    
def ttsMessage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
###############################################################
################### OPTION 2: SEND MESSAGE ####################
############# SELECT A PATIENT TO SEND MESSAGE TO #############
###############################################################
0. Back to main menu""")
    patientFile = open("patients.txt", "r")
    count = 0
    patientList = []
    for name in patientFile:
        count += 1
        patientList.append(name)
        print("{count}. {name}".format(count=count, name=name).strip())
    patientFile.close()
    option = input("Enter your option: ")
    
    if option == "0":
        options()
    else:
        try:
            if int(option) <= count:
                langMessage(patientList[int(option)-1].replace(' ', '_').strip())
            else:
                ttsMessage()
        except:
            ttsMessage()

def langMessage(topic): # TODO determine how to send message to individual patients
    os.system('cls' if os.name == 'nt' else 'clear')
    # Select language
    print("""
###############################################################
################## SELECT A LANGUAGE TO SEND ##################
###############################################################
0. Back to main menu
1. English
2. Chinese""")
    option = input("Enter your option: ")
    if option == "0":
        options()
    elif option == "1" or option == "2":
        language = "cn"
        if option == "1":
            language = "en"
        composeMessage(topic, language)
    else:
        langMessage(topic)
        
def composeMessage(topic, language):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Compose message
    print("""
###############################################################
################## COMPOSE YOUR MESSAGE #######################
###############################################################
0. Back to main menu""")
    option = input("Write your message here: ")
    if option == "0":
        pass
    else:
        # Forward message in HealthcareWorker.py
        jsonString = json.dumps({"cmd": "tts", "lang": language, "msg": option})
        hc.send_message(topic, jsonString)
    options()

def options():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Display menu
    print("""
###############################################################
####################### SELECT AN OPTION ######################
###############################################################
0. EXIT
1. CHANGE PATIENT ALERT TIME
2. SEND A MESSAGE TO A PATIENT""")
    option = input("Enter your option: ")
    if option == '0':
        exit()
    if option == '1':
        editPatient()
    elif option == '2':
        ttsMessage()
    else:
        options()


if __name__ == '__main__':    
    LED_PIN = 20
    BTN_PIN = 21
    RPI_IP = '192.168.10.136'
    
    hc = HealthcareWorker(LED_PIN, BTN_PIN, 3, 4, RPI_IP)
    piThread = Thread(target=hc.start)
    options()