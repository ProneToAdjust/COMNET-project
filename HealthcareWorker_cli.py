import os
import pickle
import HealthcareWorker

patientDictionary = {}


def setupPatient():
    print("############# OPTION 1: SETUP PATIENT #############")
    
    
    with open('patient_dictionary.pkl', 'wb') as f:
        pickle.dump(patientDictionary, f)
    pass

def editPatient():
    print("############# OPTION 2: EDIT PATIENT #############")
    
    
    with open('patient_dictionary.pkl', 'wb') as f:
        pickle.dump(patientDictionary, f)
    pass

def sendMessage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("################### OPTION 3: SEND MESSAGE ####################")
    print("############# SELECT A PATIENT TO SEND MESSAGE TO #############")
    print("###############################################################")
    print("0. Back to main menu")
    print("1. John Doe")
    print("2. Jane Doe")
    
    option = input("Enter your option: ")
    if option == 0:
        options()
    else:
        selectLanguage(int(option))
    pass

def selectLanguage(patientID):
    # Select language
    print("###############################################################")
    print("################## SELECT A LANGUAGE TO SEND ##################")
    print("###############################################################")
    print("0. Back to main menu")
    print("1. English")
    print("2. Chinese")
    option = input("Enter your option: ")
    if option == 0:
        options()
    else:
        
        
def composeMessage(patientID, language):
    # Compose message
    print("###############################################################")
    print("################## COMPOSE YOUR MESSAGE #######################")
    print("###############################################################")
    print("0. Back to main menu")
    option = input("Write your message here: ")
    if option == 0:
        options()
    else:
        

def options():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Display menu
    print("""
####################### SELECT AN OPTION ######################
1. SETUP A NEW PATIENT
2. EDIT AN EXISTING PATIENT
3. SEND A MESSAGE TO A PATIENT
###############################################################""")
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
    """
    with open('patient_dictionary.pkl', 'rb') as f:
        patientDictionary = pickle.load(f)
    
    LED_PIN = 2
    BTN_PIN = 3
    RPI_IP = ""
    hc = HealthcareWorker(LED_PIN, BTN_PIN, RPI_IP)
    hc.start()"""
    options()