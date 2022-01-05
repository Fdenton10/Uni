''' DASDA 2nd Assignment
    Student Number - 18024097
    Francis Denton'''
# Imports required to read in the many csv files
import csv

# Class for the patients
class Patient:
    # Appropriate Attributes needed for each patient
    name = ""
    status = ""
    age = 0
    weight = 0.0
    grv_limit = 0.0
    #dayClock = []

    def __init__(self,name, status, age, weight, grv_limit):
        self.name = name
        self.status = status
        self.age = age
        self.weight = weight
        self.grv_limit = weight * 5
        #self.dayClock = dayClock
    

def csv_import():
    patients = []
    patient = Patient
    dayClock = []
    hourlyData = []

    with open('PATIENT DATA - PATIENT A1.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        x = 0 
        for row in reader:
            if x == 0:
                name = "A1"
                status = row[1]
                age = filterAge(row[2])
                weight = filterWeight(row[4])
                grv_limit = weight * 5
                #print(str(status), "|", str(age), "|", str(weight), "|", str(grv_limit))
                id = patient(name, status, age, weight, grv_limit)
                patients.append(id)
                x = 3
            elif x > 2:
                hourlyData = [row[1], row[2], row[3], row[4]]
                dayClock.append(hourlyData)
            x += 1
    print(patients[0].age)

def filterWeight(weightField):
    str = weightField.replace('Weight', '')
    str = str.replace('Kg', '')
    weight = float(str)

    return weight

def filterAge(ageField):
    str = ageField.replace('Age', '')
    str = str.replace('DAYS', '')
    if "YEARS" in str:
        yearStr = str.replace('YEARS', '')
        ageInt = int(yearStr)
        age = ageInt * 365
    else:
        age = int(str)
    
    return age

def low_risk_assessment(patient):
    time_clock = 0
    day = 0
    feed = ""
    while time_clock < 24:
        if patient.weight < 40:                
            feed = "5ML"
        else:
            feed = "20ML"
        time_clock += 2

def check_grv(patient):
    print(patient[0].dayClock[3])
        