''' DASDA 2nd Assignment
    Student Number - 18024097
    Student Name - Francis Denton'''
# Imports required to read in the many csv files
import csv

# Class for the patients
class Patient:
    # variables used to keep track of number of issues the patient add and sorting them by that order
    stop_feed = 0
    score = 0
    #All info required for each of the patients
    def __init__(self,id, status, age, weight, grv_limit, dayClock):
        self.id = id
        self.status = status
        self.age = age
        self.weight = weight
        self.grv_limit = self.weight * 5
        self.dayClock = dayClock
    
    #Used to display a specific patients info on a specific day
    def patient_info(self, day_count):
        if day_count == 1:
            i, j = 0, 24
        if day_count == 2:
            i, j = 24, 48
        if day_count == 3:
            i, j = 48, 72
        if day_count == 4:
            i, j = 72, 96
        if day_count == 5:
            i, j = 96, 120
        print("Patient: ",self.id, " Day: ", str(day_count))
        print("----------------------")
        print("[Time, Feed, Grv, Issues]")
        while i < j:
            print("[",str(self.dayClock[i].time), ",",str(self.dayClock[i].feed),",", str(self.dayClock[i].grv),",", str(self.dayClock[i].issues),"]")
            i += 1

#Class for patient data for the 5 daay cycle
class HourlyData:
    def __init__(self, time, feed, grv, issues):
        self.time = time
        self.feed = feed
        self.grv = grv
        self.issues = issues

#Function to import and initially assign patient data to their appropriate variables
def csv_import(patients, filename, patient_id):
    print(patient_id + " Data Loaded")
    patient, hour = Patient, HourlyData
    #List to hold the data about patients treatment over the 5 days
    dayClock = []

    #Reads in the file
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        x = 0 
        for row in reader:
            #Takes the first row of the csv and takes in the patients id, weight, age and grv_limit
            if x == 0:
                id, status = patient_id, row[1]
                weight = filterWeight(row[4]) 
                age, grv_limit = filterAge(row[2]), float(weight * 5)
                x += 1
            #Assigns all of the time specific data based on its column in a row of the csv
            elif x > 3:
                time, feed, grv, issues = row[1], row[2], row[3], row[4]
                #Adds the instance of the class to the dayCLock list
                dayClock.append(hour(time, feed, grv, issues))
            x += 1
    #Creates an instance of the patient class
    patient_ = patient(id, status, age, weight, grv_limit, dayClock)
    #Adds the instance to the list of patients
    patients.append(patient_)

#Function to convert the weight value from a string to a float in order to perform numerical operations on.
def filterWeight(weightField):
    #Removes all the text from the weight field
    str = weightField.replace('Weight', '')
    str = str.replace('Kg', '')
    #Convers from string to float
    weight = float(str)

    #return weight value
    return weight

#Function to convert the age value from a string to an int in order to process data
def filterAge(ageField):
    #Removes all the text from the age field
    str = ageField.replace('Age', '')
    str = str.replace('DAYS', '')
    #Converts to a large number to differentiate between the number of days and years
    if "YEARS" in str:
        yearStr = str.replace('YEARS', '')
        ageInt = int(yearStr)
        age = ageInt * 365
    else:
        age = int(str)
    
    #return age value
    return age

#Checks patient status and calls the low or high risk function dependant on result
def status_check(patient, day_count):
    if patient.status == "LR":
        lr_assessment(patient, day_count)
    if patient.status == "HR":
        hr_assessment(patient, day_count)

#Depending on the day count, calls the run_day function using different hour thresholds
# e.g day 1 = 0 - 24 hours, day 2 = 24 - 48 hours etc
def lr_assessment(patient, day_count):
    if day_count == 1:
        run_day(patient, 24, 23, 0)
        # If patients weight is > 40, assigns them their initial feed for the first 4 hours
        if patient.weight > 40:
            patient.dayClock[0].feed = '20ML /2 hrs'
            patient.dayClock[2].feed = '20ML /2 hrs'
    if day_count == 2:
        run_day(patient, 48, 47, 24)
    if day_count == 3:
        run_day(patient, 72, 71, 48)
    if day_count == 4:
        run_day(patient, 96, 95, 72)
    if day_count == 5:
        run_day(patient, 120, 119, 96)

def final_day(listname):
    #Calls function to sort the list by lowest amount of issues first
    selection_sort(listname)
    #Prints all patient final issues over the 5 days
    for i in range(len(listname)):
        print("Patient",str(listname[i].id),":", str(listname[i].dayClock[23].issues),",", str(listname[i].dayClock[47].issues),",", 
        str(listname[i].dayClock[71].issues), ",",str(listname[i].dayClock[95].issues),",", str(listname[i].dayClock[119].issues))
    #Prompts the user to see if they want to see patient info for a specific day
    print("-----------------------")
    print("1. See patient info?")
    print("Press any other key to exit")
    choice = input()
    if choice == "1":
        #Asks for the patient ID they would like to see data for and which day
        search = input("What patient would you like to see info for: ")
        number_day = int(input("What day?"))
        for i in range(len(listname)):
            if search == listname[i].id:
                #Calls the patient info function once a match has been found of a patient ID
                listname[i].patient_info(number_day)

def selection_sort(listname):        
    for i in range(len(listname)):
        minimum = i
        
        for j in range(i + 1, len(listname)):
            # Select the smallest value
            if listname[j].score < listname[minimum].score:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        listname[minimum], listname[i] = listname[i], listname[minimum]

    #Returns sorted list   
    return listname

def run_day(patient, i, j, k):
    #Sets hour threshold for which day it is
    hour_counter = k
    #While its lower than the final hour for that day
    while hour_counter < i:
        #Check if the grv is a number
        if patient.dayClock[hour_counter].grv.isnumeric():
            #Checks to see if is is over the patient limit, if so, STOPPED FEEDINGing and change issue column
            if float(patient.dayClock[hour_counter].grv) > patient.grv_limit:
                patient.dayClock[hour_counter].feed = '0/ML /2 HRS'
                patient.dayClock[hour_counter].issues = 'STOPPED FEEDING'
                patient.stop_feed += 1
                #If patients feed has been stopped more than twice, refer them to a dietician
                if patient.stop_feed > 2:
                    patient.dayClock[j].issues = "REFER TO DIETICIAN"
                else:
                    patient.dayClock[j].issues = "STOPPED FEEDING"  
            else:
                #If no issues have occured, assign patient their feed depending on their weight
                #If under 40kg, weight beomes 10ML /2hrs, if over weight beomes 30ML/2hrs
                if patient.weight < 40:
                    patient.dayClock[hour_counter].feed = '10ML /2 HRS'
                    if hour_counter > 4  and hour_counter < 118:
                        patient.dayClock[hour_counter + 2].feed = '10ML /2 HRS'              
                else:                   
                    patient.dayClock[hour_counter].feed = '30ML /2 HRS' 
                    if hour_counter > 4  and hour_counter < 118:
                        patient.dayClock[hour_counter + 2].feed = '30ML /2 HRS'      
        #If patient issues is neither STOPPED FEEDINGing or refer to dietician, then no issues are found             
        if patient.dayClock[hour_counter].issues != "STOPPED FEEDING":
            if patient.dayClock[hour_counter].issues !="REFER TO DIETICIAN":
                patient.dayClock[hour_counter].issues = "NONE"
        hour_counter += 1
    #If the final issue for that day is STOPPED FEEDINGing or refer to dietician then their score is increased
    if patient.dayClock[j].issues == "STOPPED FEEDING":
            patient.score += 1
    elif patient.dayClock[j].issues =="REFER TO DIETICIAN":
            patient.score += 1

def day_end(listname, day_count):
    print("At the end of Day: ", str(day_count))
    #For the first 4 days, the list is not sorted, so patient issues are displayed in order of ID
    if day_count <= 4:
        print("------------------------")
        for i in listname:
            #Calls function to get issues for patients each day
            get_issue(i, day_count)
        print("------------------------")
        input("Hit any key to proceed to the next day:")
    print("------------------------")
    #Calls the final day function to call the sorted list of patients by their issues
    if day_count == 5:
        final_day(listname)

#Function used to print out patients issues depending on the day, and the previous days up that
def get_issue(patient, day_count):
    if day_count == 1:
        print("Patient",str(patient.id),":", str(patient.dayClock[23].issues))
    if day_count == 2:
        print("Patient",str(patient.id),":", str(patient.dayClock[23].issues),",", str(patient.dayClock[47].issues))
    if day_count == 3:
        print("Patient",str(patient.id),":", str(patient.dayClock[23].issues),",", str(patient.dayClock[47].issues),",", 
        str(patient.dayClock[71].issues))
    if day_count == 4:
        print("Patient",str(patient.id),":", str(patient.dayClock[23].issues),",", str(patient.dayClock[47].issues),",", 
        str(patient.dayClock[71].issues), ",",str(patient.dayClock[95].issues))

#High risk patients assessment
def hr_assessment(patient, day_count):
    hour_counter = 0
    #No issues for first 3 days
    if day_count <= 3:
        while hour_counter < 72:
            #Format change from ['NONE'] to NONE, keep it consistent with low risk patients
            patient.dayClock[hour_counter].issues = "NONE"
            hour_counter += 1
    #Change to low risk after day three
    if day_count == 4:
        lr_assessment(patient, 4)
    if day_count == 5:
        lr_assessment(patient, 5)

#Runs the program, calling the appropriate functions for the beginning and end of the day
def run(listname):
    print("------------------------")
    print("Welcome to the PICU System:")
    print("------------------------")
    x = 1
    while x < 6:
        for patient in listname:
            #Calls function to check patient status each day
            status_check(patient, x)
        #Calls Function to get information at the end of each day
        day_end(listname, x)
        x += 1

def initial_boot():
    # Creates list to hold patients in
    patients = []
    # Creates patient_id's and calls the import function to read in each file
    patient_id = "A1"
    csv_import(patients, "PATIENT DATA - PATIENT A1.csv", patient_id)
    patient_id = "A2"
    csv_import(patients, "PATIENT DATA - PATIENT A2.csv", patient_id)
    patient_id = "A3"
    csv_import(patients, "PATIENT DATA - PATIENT A3.csv", patient_id)
    patient_id = "B1"
    csv_import(patients, "PATIENT DATA - PATIENT B1.csv", patient_id)
    patient_id = "B2"
    csv_import(patients, "PATIENT DATA - PATIENT B2.csv", patient_id)
    patient_id = "B3"
    csv_import(patients, "PATIENT DATA - PATIENT B3.csv", patient_id)
    patient_id = "B4"
    csv_import(patients, "PATIENT DATA - PATIENT B4.csv", patient_id)
    patient_id = "B5"
    csv_import(patients, "PATIENT DATA - PATIENT B5.csv", patient_id)
    patient_id = "B6"
    csv_import(patients, "PATIENT DATA - PATIENT B6.csv", patient_id)
    patient_id = "B7"
    csv_import(patients, "PATIENT DATA - PATIENT B7.csv", patient_id)
    #Calls function to run program
    run(patients)

initial_boot()