import os
import pickle
from HealthcareWorker import HealthcareWorker
from threading import Thread

#patientDictionary = {}
hc = None
piThread = None

def setupPatient():
    print("############# OPTION 1: SETUP PATIENT #############")
    
    
    #with open('patient_dictionary.pkl', 'wb') as f:
    #    pickle.dump(patientDictionary, f)
    pass

def editPatient():
    print("############# OPTION 2: EDIT PATIENT #############")
    
    
    #with open('patient_dictionary.pkl', 'wb') as f:
    #    pickle.dump(patientDictionary, f)
    pass

def ttsMessage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
###############################################################
################### OPTION 3: SEND MESSAGE ####################
############# SELECT A PATIENT TO SEND MESSAGE TO #############
###############################################################
0. Back to main menu""")
    print("1. John Doe")
    print("2. Jane Doe")
    
    option = input("Enter your option: ")
    if option == "0":
        options()
    elif option == "1" or option == "2": # if patient exists
        langMessage(int(option))
    else:
        ttsMessage()

def langMessage(patientID): # TODO determine how to send message to individual patients
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
        composeMessage(patientID, language)
    else:
        langMessage(patientID)
        
def composeMessage(patientID, language):
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
        language = language + ":"
        fullQuery = "tts:" + language + option
        hc.on_send_message(fullQuery)
    options()

def options():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Display menu
    print("""
###############################################################
####################### SELECT AN OPTION ######################
###############################################################
1. SETUP A NEW PATIENT
2. EDIT AN EXISTING PATIENT
3. SEND A MESSAGE TO A PATIENT""")
    option = input("Enter your option: ")
    if option == '1':
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
    
    LED_PIN = 2
    BTN_PIN = 3
    RPI_IP = "192.168.10.136"
    
    hc = HealthcareWorker(LED_PIN, BTN_PIN, RPI_IP)
    piThread = Thread(target=hc.start)
    #hc.start()
    options()