import os
import pickle
import HealthcareWorker

patientDictionary = {}


def setupPatient(message):
    print("############# OPTION 1: SETUP PATIENT #############")
    
    
    with open('patient_dictionary.pkl', 'wb') as f:
        pickle.dump(patientDictionary, f)
    pass

def editPatient(message):
    print("############# OPTION 2: EDIT PATIENT #############")
    
    
    with open('patient_dictionary.pkl', 'wb') as f:
        pickle.dump(patientDictionary, f)
    pass

def sendMessage(message):
    print("############# OPTION 3: SEND MESSAGE #############")
    print("############# SELECT A PATIENT TO SEND MESSAGE TO #############")
     
    pass

def options():
    # Show status of all patients
    
    
    # Display menu
    print("""
            ############# SELECT AN OPTION #############
            1. SETUP A NEW PATIENT
            2. EDIT AN EXISTING PATIENT
            3. SEND A MESSAGE TO A PATIENT
            ############################################
            """)
    option = input("Enter your option: ")
    if option == '1':
        setupPatient()
    elif option == '2':
        editPatient()
    elif option == '3':
        sendMessage()
    else:
        options()


if __name__ == '__main__':
    with open('patient_dictionary.pkl', 'rb') as f:
        patientDictionary = pickle.load(f)
    LED_PIN = 2
    BTN_PIN = 3
    RPI_IP = ""
    hc = HealthcareWorker(LED_PIN, BTN_PIN, RPI_IP)
    hc.start()
    options()