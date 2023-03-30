import os
from HealthcareWorker import HealthcareWorker
from threading import Thread
import json

#patientDictionary = {}
hc = None
piThread = None

def setupPatient():
    print("############# OPTION 1: SETUP PATIENT #############")
    
    
    pass

def editPatient():
    print("""
###############################################################
################### OPTION 2: EDIT PATIENT ####################
############# SELECT A PATIENT TO EDIT INFORMATION ############
###############################################################
0. Back to main menu""")
    patientFile = open("patients.txt", "r")
    count = 0
    for name in patientFile:
        count += 1
        print("{count}. {name}".format(count=count, name=name))
    patientFile.close()
    option = input("Enter your option: ")
    

def ttsMessage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
###############################################################
################### OPTION 3: SEND MESSAGE ####################
############# SELECT A PATIENT TO SEND MESSAGE TO #############
###############################################################
0. Back to main menu""")
    patientFile = open("patients.txt", "r")
    count = 0
    patientList = []
    for name in patientFile:
        count += 1
        patientList.append(name)
        print("{count}. {name}".format(count=count, name=name))
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
        hc.on_send_message(topic, jsonString)
    options()

def options():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Display menu
    print("""
###############################################################
####################### SELECT AN OPTION ######################
###############################################################
0. EXIT
1. SETUP A NEW PATIENT
2. EDIT AN EXISTING PATIENT
3. SEND A MESSAGE TO A PATIENT""")
    option = input("Enter your option: ")
    if option == '0':
        exit()
    elif option == '1':
        setupPatient()
    elif option == '2':
        editPatient()
    elif option == '3':
        ttsMessage()
    else:
        options()


if __name__ == '__main__':
    
    # with open('patient_dictionary.pkl', 'rb') as f:
    #     patientDictionary = pickle.load(f)
    
    LED_PIN = GPIO_PIN_NO
    BTN_PIN = GPIO_PIN_NO
    RPI_IP = 'RPI IP HERE'
    
    hc = HealthcareWorker(LED_PIN, BTN_PIN, 3, 4, RPI_IP)
    piThread = Thread(target=hc.start)
    options()