import datetime
from pymongo import MongoClient
import csv

client = MongoClient(port=27017)
db = client["ADB"]


def date_conversion(date):
    date = date.split('/')
    d = datetime.datetime.strptime(
        "{0}-{1}-{2}".format(date[2], date[1], date[0]), "%Y-%m-%d")
    return d

def string_to_float(value):
    Float = float(value)
    print(Float)
    return Float


def import_to_mongo():
    patients = db["patients"]
    with open("data.csv", 'r') as csvfile:
        line = 0
        datareader = csv.reader(csvfile)
        documents = []
        for row in datareader:
            if line > 0:
                # Construct document for the current patient
                patient_in_doc = False
                if len(documents) > 0:
                    for doc in documents:
                        if doc["name"] == row[0]:
                            patient_in_doc = True
                if not patient_in_doc:
                    doc = {
                        "name": row[0],
                        "dob": date_conversion(row[1]),
                        "sex": row[2],
                        "address": {
                            "street_address": row[3],
                            "city": row[4],
                            "postcode": row[5],
                            "phoneNo": row[6],
                        },
                        "admissions": [{
                            "admissionDate": date_conversion(row[7]),
                            "height(m)": string_to_float(row[8]),
                            "weight(kg)": string_to_float(row[9]),
                            "BMI": string_to_float(row[10]),
                            "bodyType": row[11],
                            "smoker": row[12],
                            "asthmatic": row[13],
                            "njt_ngr": row[14],
                            "hypertension": row[15],
                            "rentalRT": row[16],
                            "ileostomyColostomy": row[17],
                            "parentalNeutrition": row[18],
                            "referralDecision": row[19],
                        }]
                    }
                    documents.append(doc)
                else:
                    doc["admissions"].append({
                        "admissionDate": date_conversion(row[7]),
                        "height(m)": string_to_float(row[8]),
                        "weight(kg)": string_to_float(row[9]),
                        "BMI": string_to_float(row[10]),
                        "bodyType": row[11],
                        "smoker": row[12],
                        "asthmatic": row[13],
                        "njt_ngr": row[14],
                        "hypertension": row[15],
                        "rentalRT": row[16],
                        "ileostomyColostomy": row[17],
                        "parentalNeutrition": row[18],
                        "referralDecision": row[19],
                    })
            line += 1
        patients.insert_many(documents)
        print(documents)


import_to_mongo()
