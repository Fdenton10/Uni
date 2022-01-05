import csv

# Lists - Necessary lists for the three csv files.
pet_list = []
wild_list = []
treatment_list = []


# Treatment - Class used to hold all of the data contained in the treatment csv file
class Treatment:
    # Attributes that occur for items in the treatment class
    sanctuaryid = ""
    surgery = ""
    surgeryd = ""
    med = ""
    meds = ""
    medf = ""
    abuse = ""
    abandon = ""

    # Initialising an instance of the class and assigning values to its attributes
    def __init__(self, sanctuaryid, surgery, surgeryd, med, meds, medf, abuse, abandon):
        self.sanctuaryid = sanctuaryid
        self.surgery = surgery
        self.surgeryd = surgeryd
        self.med = med
        self.meds = meds
        self.medf = medf
        self.abuse = abuse
        self.abandon = abandon

    # Function which provides all of the information about one of the objects of the class
    def display_info(self):
        treatment_info = "\nSanctuary ID: " + self.sanctuaryid + "\nSurgery Type: " + self.surgery + "\nSurgery Date: " + \
                         self.surgeryd + "\nMedication: " + self.med + "\nMedication Start Date: " + \
                         self.meds + "\nMedication Finish Date: " + self.medf + "\nResponsible for Abuse: " + self.abuse + \
                         "\nResponsible for Abandon: " + self.abandon

        return treatment_info


# Main Class - Animal - Used to create objects for each row of a file. Attributes being the column headers.
class Animal:
    # Attributes that occur in both pets and wild animals
    sanctuaryid = ""
    type = ""
    vaccinated = ""
    admission = ""
    datea = ""
    dated = ""
    dest = ""
    desta = ""

    # Function which will display all of the information about an object
    def __init__(self, sanctuaryid, type, vaccinated, admission, datea, dated, dest, desta):
        self.sanctuaryid = sanctuaryid
        self.type = type
        self.vaccinated = vaccinated
        self.admission = admission
        self.datea = datea
        self.dated = dated
        self.dest = dest
        self.desta = desta


#  Class for the pet subtype of animal. Subclass of the Animal class.
class Pet(Animal):
    # Attributes unique to pets which wild animals do not share
    breed = ""
    neutered = ""
    micro = ""

    # All of the attributes of a pet, initialising them
    def __init__(self, sanctuaryid, type, breed, vaccinated, neutered, micro, admission, datea, dated, dest, desta):
        self.sanctuaryid = sanctuaryid
        self.type = type
        self.breed = breed
        self.vaccinated = vaccinated
        self.neutered = neutered
        self.micro = micro
        self.admission = admission
        self.datea = datea
        self.dated = dated
        self.dest = dest
        self.desta = desta

    # Function which will display all of the information about an object
    def display_info(self):
        pet_info = "\nSanctuary ID: " + self.sanctuaryid + "\nAnimal Type: " + self.type + "\nAnimal Breed: " + \
                   self.breed + "\nVaccinated?: " + self.vaccinated + "\nNeutered? " + self.neutered + \
                   "\nMicrochip Number: " + self.micro + "\nReason for admission: " + self.admission + \
                   "\nArrival date: " + self.datea + "\nDeparture date: " + self.dated + "\nDestination: " \
                   + self.dest + "\nDestination address: " + self.desta

        return pet_info


#  Class for the wild subtype of animal. Subclass of the Animal class. Inherits attributes contained in main class
class Wild(Animal):
    # All of the attributes of a wild animal, initialising them
    def __init__(self, sanctuaryid, type, vaccinated, admission, datea, dated, dest, desta):
        self.sanctuaryid = sanctuaryid
        self.type = type
        self.vaccinated = vaccinated
        self.admission = admission
        self.datea = datea
        self.dated = dated
        self.dest = dest
        self.desta = desta

    # Function which will display all of the information about an object
    def display_info(self):
        wild_info = "Sanctuary ID: " + self.sanctuaryid + "\nAnimal Type: " + self.type + "\nVaccinated?: " \
                    + self.vaccinated + "\nReason for admission: " + self.admission + \
                    "\nArrival date: " + self.datea + "\nDeparture date: " + self.dated + "\nDestination: " \
                    + self.dest + "\nDestination address: " + self.desta

        return wild_info


# Opening and reading the file data. Putting them into dictionaries in order to create objects for the animals keys and
# then putting them into objects list in order to manipulate the information later.
with open('PetData.csv', 'r') as petFile:
    preader = csv.DictReader(petFile)
    for row in preader:
        pet_list.append(Pet(row['Sanctuary Identification'], row['Type'], row['Breed'], row['Vaccinated'],
                            row['Neutered'], row['Microchip Number'], row['Reason for admission'],
                            row['Date of Arrival'], row['Date of Departure'], row['Destination'],
                            row['Destination Address']))
with open('WildData.csv', 'r') as wildFile:
    wreader = csv.DictReader(wildFile)
    for row in wreader:
        wild_list.append(Wild(row['Sanctuary Identification'], row['Type'], row['Vaccinated'],
                              row['Reason for admission'], row['Date of Arrival'], row['Date of Departure'],
                              row['Destination '], row['Destination Address']))
with open('TreatmentData.csv', 'r') as treatmentFile:
    treader = csv.DictReader(treatmentFile)
    for row in treader:
        treatment_list.append(Treatment(row['Sanctuary Identification'], row['Surgery'], row['Surgery Date'],
                                        row['Medication '], row['Medication Start'], row['Medication Finish'],
                                        row['Responsible for Abuse'], row['Responsible for Abandoning']))


# Menu to for program, allows for navigation from the user
def menu():
    while True:
        print("\nWelcome to the UWE Animal Sanctuary system. Please select an option below.")
        print("1. Add data for ma new arrival" + "\n" + "2. View Data" + "\n" + "3. Edit Data" + "\n" + "4. Exit")
        menuchoice = input("Option: ")
        if menuchoice == "1":
            new_arrival()
        elif menuchoice == "2":
            view_list()
        elif menuchoice == "3":
            edit_list()
        elif menuchoice == "4":
            exit()
            break


# Presents list of options available to edit for the user upon request
def edit_list():
    print("\n1. Edit Microchip Number" + "\n2. Edit Details of Neutering" +
          "\n3. Edit Date of Departure from sanctuary" +
          "\n4. Edit Destination of the animal departure" +
          "\n5. Edit Details of Surgery")
    choice = input("What Information would you like to edit?: ")
    if choice == "1":
        # Calls function for user to edit microchip numbers in pets
        chip_edit()
    elif choice == "2":
        # Calls function for user to edit neutered status in pets
        neuter_edit()
    elif choice == "3":
        # Calls function for user to edit departure date for animals
        dep_date_edit()
    elif choice == "4":
        # Calls function for user to edit departure destination for animals
        dep_dest_edit()
    elif choice == "5":
        # Calls function for the user to edit surgery
        edit_surgery()


# Presents list of options for data available to view for the user upon request
def view_list():
    print("\n" + "Available Information" + "\n" + "1. Animal information for a specific ID" + "\n"
          + "2. List of Dogs Available for Adoption" + "\n"
          + "3. List of Cats Available for Adoption" + "\n"
          + "4. List of Animals who are ready to be return to their owners" + "\n"
          + "5. List of Owners who have previously abused animals" + "\n"
          + "6. List of Owners who have previously abandoned animals" + "\n")
    choice = input("What Information would you like to view?: ")
    if choice == "1":
        # Calls function which allows for user to enter a sanctuary ID and recieve all information about that animal
        animal_data()
    elif choice == "2":
        # Calls function which displays the list of dogs available for adoption
        dog_list()
    elif choice == "3":
        # Calls function which displays the list of cats available for adoption
        cat_list()
    elif choice == "4":
        # Calls function which displays the list of animals that are ready to be returned to their owners
        return_to_owner()
    elif choice == "5":
        # Calls function which displays the list of owners who have abused animals in the past
        abuse_owner()
    elif choice == "6":
        # Calls function which displays the list of owners who have abandoned animals in the past
        abandon_owner()
    else:
        print("Invalid Value, Returning to Main Menu")
        menu()


# Used to rewrite the pet file after changes have been made to any of the attributes of a pet
def write_pet():
    # Opens the file so we can write to it
    with open('PetData.csv', 'w', newline='') as writepet:
        write_p = csv.writer(writepet, delimiter=",")
        # Creates the header row for all of the column headers
        write_p.writerow(['Sanctuary Identification', 'Type', 'Breed', 'Vaccinated', 'Neutered',
                          'Microchip Number', 'Reason for admission',
                          'Date of Arrival', 'Date of Departure',
                          'Destination', 'Destination Address'])
        # Fills out a row with all of the values assigned to each pet in the sanctuary
        for pet in pet_list:
            write_p.writerow([pet.sanctuaryid, pet.type, pet.breed, pet.vaccinated, pet.neutered,
                              pet.micro, pet.admission, pet.datea, pet.dated,
                              pet.dest, pet.desta])


# Used to rewrite the pet file after changes have been made to any of the attributes of the treatment csv
def write_treatment():
    # Opens the file so we can write to it
    with open('TreatmentData.csv', 'w', newline='') as writetreatment:
        write_t = csv.writer(writetreatment, delimiter=",")
        # Creates the header row for all of the column headers
        write_t.writerow(['Sanctuary Identification', 'Surgery', 'Surgery Date',
                          'Medication ', 'Medication Start', 'Medication Finish',
                          'Responsible for Abuse', 'Responsible for Abandoning'])
        # Fills out a row with all of the values assigned to each animal that has undergone treatment
        for treatment in treatment_list:
            write_t.writerow([treatment.sanctuaryid, treatment.surgery, treatment.surgeryd, treatment.med,
                              treatment.meds, treatment.medf, treatment.abuse, treatment.abandon])


# Used to rewrite the pet file after changes have been made to any of the attributes of a wild animal
def write_wild():
    # Opens the file so we can write to it
    with open('WildData.csv', 'w', newline='') as writewild:
        write_w = csv.writer(writewild, delimiter=",")
        # Creates the header row for all of the column headers
        write_w.writerow(['Sanctuary Identification', 'Type', 'Vaccinated',
                          'Reason for admission', 'Date of Arrival', 'Date of Departure',
                          'Destination ', 'Destination Address'])
        # Fills out a row with all of the values assigned to each wild animal in the sanctuary
        for wild in wild_list:
            write_w.writerow([wild.sanctuaryid, wild.type, wild.vaccinated, wild.admission, wild.datea, wild.dated,
                              wild.dest, wild.desta])


# Function to edit the microchip number of pets
def chip_edit():
    id = input("Please enter the id of the animal who you wish to assign a chip number to: ")
    # Loops through the list to check whether the inputted value
    # is equal to an existing sanctuary ID so we can assign it a new chip value
    for i in range(0, len(pet_list)):
        # finds index of matching id
        if id == pet_list[i].sanctuaryid:
            # Allows user to enter new value for microchip
            chip = input("Please input chip number to assign (Format of D + 6 numbers): ")
            # Changes value to the newly entered
            pet_list[i].micro = chip
            # Displays new information about the animal
            print(pet_list[i].display_info())
            # Updates the csv file with new information
            write_pet()


# Function to edit the nuetered value for an animal
def neuter_edit():
    # Loops through the list to check whether the inputted value
    # is equal to an existing sanctuary ID so we can assign it a new neutered status
    id = input("Please enter the id of the animal who you wish to change the neutered status of: ")
    for i in range(0, len(pet_list)):
        # finds index of matching id
        if id == pet_list[i].sanctuaryid:
            # Allows user to enter new value for neuter status
            neuter = input("Please input neuter status (Either Yes or Leave blank): ")
            pet_list[i].neutered = neuter
            # Displays new information about the animal
            print(pet_list[i].display_info())
            # Updates the csv file with new information
            write_pet()


# Function to edit the departure date of an animal
def dep_date_edit():
    id = input("Please enter the id of the animal who you wish to change the neutered status of: ")
    # Checks to see whether the user wants the change this attribute for a pet or wild animal
    # For Pet
    if id[0] == "P":
        for i in range(0, len(pet_list)):
            # Checks for matching ID
            if id == pet_list[i].sanctuaryid:
                datedep = input("Please input departure date (Format - DD/MM/YYYY): ")
                # Updates to new value
                pet_list[i].dated = datedep
                # Displays new information about the animal
                print(pet_list[i].display_info())
                # Updates the csv file with new information
                write_pet()
    # For Wild
    if id[0] == "W":
        for i in range(0, len(wild_list)):
            # Checks for matching ID
            if id == wild_list[i].sanctuaryid:
                datedep = input("Please input departure date (Format - DD/MM/YYYY): ")
                # Updates to new value
                wild_list[i].dated = datedep
                # Displays new information about the animal
                print(wild_list[i].display_info())
                # Updates the csv file with new information
                write_wild()


# Function to edit the surgery information of an animal
def edit_surgery():
    id = input("Please enter the id of the animal who you wish to change surgery information for: ")
    for i in range(0, len(treatment_list)):
        # Checks for matching ID
        if id == treatment_list[i].sanctuaryid:
            # Takes in inputs for new values the surgery information
            surgery = input("Please Enter Surgery type: ")
            surgeryd = input("Please input date of surgery (format DD/MM/YYYY - Include '/'): ")
            med = input("Medication type (if any): ")
            med_s = input("Please input medication start date (format DD/MM/YYYY - Include '/'): ")
            med_f = input("Please input medication finish date (format DD/MM/YYYY - Include '/'): ")
            # If nothing has been inputted it wont replacing existing values
            # e.g. if only assigning medication wont update surgery to blank values
            if surgery != "":
                treatment_list[i].surgery = surgery
            if surgeryd != "":
                treatment_list[i].surgeryd = surgeryd
            if med != "":
                treatment_list[i].med = med
            if med_s != "":
                treatment_list[i].meds = med_s
            if med_f != "":
                treatment_list[i].meds = med_f
            # Displays the updated information
            print(treatment_list[i].display_info())
            # Updates csv
            write_treatment()


# Function to edit the destination date of an animal
def dep_dest_edit():
    id = input("Please enter the id of the animal who you wish to change the departure destination of: ")
    # Checks for if user wantss to update pet or wild animal
    if id[0] == "P":
        for i in range(0, len(pet_list)):
            # Checks for matching ID
            if id == pet_list[i].sanctuaryid:
                # Takes in new values
                destination = input("Please enter the destination of the animal")
                destaddress = input("Please input departure date (Format - DD/MM/YYYY): ")
                # Updates existing values
                pet_list[i].dest = destination
                pet_list[i].desta = destaddress
                # Displays the updated information
                print(pet_list[i].display_info())
                # Updates csv
                write_pet()
    if id[0] == "W":
        for i in range(0, len(wild_list)):
            if id == wild_list[i].sanctuaryid:
                # Takes in new values
                destination = input("Please enter the destination of the animal")
                destaddress = input("Please input departure date (Format - DD/MM/YYYY): ")
                # Updates existing values
                wild_list[i].dest = destination
                wild_list[i].desta = destaddress
                # Displays the updated information
                print(wild_list[i].display_info())
                # Updates csv
                write_wild()


# Sorting Algorithm in order to reorder the lists to display information in order of number or alphabetical
def bubble_sort(file):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(file) - 1):
            if file[i] > file[i + 1]:
                # Swap the elements
                file[i], file[i + 1] = file[i + 1], file[i]
                # Set the flag to True so we'll loop again
                swapped = True
    print(file)


# Menu option in order to display information for one of the animals.
def animal_data():
    anitype = input("Pet or Wild data?: ")
    # Asks for animal category
    if anitype == "Wild" or anitype == "wild":
        id_search = input("Please search for an animal ID: ")
        for i in range(0, len(wild_list)):
            # Finds matching ID to the one entered
            if id_search == wild_list[i].sanctuaryid:
                # Prints info about chosen animal
                print(wild_list[i].display_info())
    elif anitype == "Pet" or anitype == "pet":
        id_search = input("Please search for an animal ID: ")
        for i in range(0, len(pet_list)):
            # Finds matching ID to the one entered
            if id_search == pet_list[i].sanctuaryid:
                # Prints info about chosen animal
                print(pet_list[i].display_info())
    else:
        print("Invalid value, returning to main menu")
        menu()


# Creating a new pet arrival
def new_pet():
    # Opens new file to write too
    with open('PetData.csv', 'a')as wpet_file:
        wpet = csv.writer(wpet_file, lineterminator='\n')

        sanctuary_identifier = input("Sanctuary Identifier (format example - P00000): ")
        # Verifies whether the entered animal ID exists. If not allows for another entry
        for i in range(0, len(pet_list)):
            while sanctuary_identifier == pet_list[i].sanctuaryid:
                print("Id already found in treatment list, please insert new ID into the system")
                sanctuary_identifier = input("Please enter ID")
        # Makes sure format of entered ID is correct
        while sanctuary_identifier[0] != "P":
            print("Error Invalid ID Format, Try again")
            sanctuary_identifier = input()
        type = input("Type of Animal: ")
        breed = input("Breed: ")
        vaccinated = input("Vaccinated?: ")
        neutered = input("Neutered: ")
        chip = input("Microchip Number (Format D######): ")
        admission = input("Reason for Admission: ")
        datea = input("Arrival Date (format : DD/MM/YYYY): ")
        dated = input("Departure Date (format : DD/MM/YYYY): ")
        dest = input("Destination: ")
        desta = input("Destination Address: ")
        # Writes the newly entered information into the csv file
        wpet.writerow(
            [sanctuary_identifier, type, breed, vaccinated, neutered, chip, admission, datea, dated, dest, desta])


# Creating a new treatment information
def new_surgery():
    with open('TreatmentData.csv', 'a', newline="") as wtreatment_file:
        wtreat = csv.writer(wtreatment_file, lineterminator='\n')

        sanctuary_identifier = input("Sanctuary Identifier (Format e.g WA000000 or P00000): ")
        # Checks to see whether inputted value is already present in treatment list
        for i in range(0, len(treatment_list)):
            while sanctuary_identifier == treatment_list[i].sanctuaryid:
                print("Id already found in treatment list, please insert new ID into the system")
                sanctuary_identifier = input("Please enter ID")
        # Checks to ses if format of ID is acceptable
        while sanctuary_identifier[0] != "W" and sanctuary_identifier[1] != "A" and sanctuary_identifier[0] != "P":
            print("Error Invalid ID Format, Please Try again")
            sanctuary_identifier = input()
        surgery = input("Surgery Type: ")
        surgery_date = input("Date of Surgery: ")
        med = input("Type of medication: ")
        meds = input("Medication Start Date: ")
        medf = input("Medication Finish Date: ")
        abuse = input("Responsible for Abuse: ")
        abandon = input("Responsible for Abandoning")
        # Writes news info into the csv file
        wtreat.writerow([sanctuary_identifier, surgery, surgery_date, med, meds, medf, abuse, abandon])


# Creating a new wild arrival
def new_wild():
    with open('WildData.csv', 'a')as wwild_file:
        # Opens new file to write too
        wwild = csv.writer(wwild_file, lineterminator='\n')

        sanctuary_identifier = input("Sanctuary Identifier (format example - WA000000): ")
        # Verifies whether the entered animal ID exists. If not allows for another entry
        for i in range(0, len(wild_list)):
            while sanctuary_identifier == wild_list[i].sanctuaryid:
                print("Id already found in treatment list, please insert new ID into the system")
                sanctuary_identifier = input("Please enter ID")
        # Makes sure format of ID is correct
        while sanctuary_identifier[0] != "W" and sanctuary_identifier[1] != "A":
            print("Error Invalid Value, Try again")
            sanctuary_identifier = input()
        type = input("Type of Animal: ")
        vaccinated = input("Vaccinated?: ")
        admission = input("Reason for Admission: ")
        datea = input("Arrival Date (format : DD/MM/YYYY): ")
        dated = input("Departure Date (format : DD/MM/YYYY): ")
        dest = input("Destination: ")
        desta = input("Destination Address: ")
        # Writes new info to csv file
        wwild.writerow([sanctuary_identifier, type, vaccinated, admission, datea, dated, dest, desta])


# Deciding what type of new information the user wishes to enter
def new_arrival():
    type = input("What would you like to do? " + "\n1. Create new animal" + "\n2. Enter details of a new surgery ")
    if type == "1":
        # Asks which animal type they wish to create data for
        arrival = input("Would you like to create data for a new pet or wild animal ")
        if arrival == "wild" or arrival == "Wild":
            # Calls function to create a new wild animal
            new_wild()
        elif arrival == "pet" or arrival == "Pet":
            # Calls function to create a new pet in the system
            new_pet()
        else:
            print("Invalid Value Entered, Please try again")
            new_arrival()
    # Calls surgery function if they need to create new information
    if type == "2":
        new_surgery()

# Creates the list of dogs ready for adoption
def dog_list():
    print("\n" + "Dogs ready for adoption:")
    # Checks for all of the animals which meet the conditions required before you can be ready for adoption
    for i in range(0, len(pet_list) - 1):
        if pet_list[i].type == "Dog" and pet_list[i].vaccinated == "Yes" and pet_list[i].neutered == "Yes" \
                and pet_list[i].micro != "":
            # Prints out the list of dog ID's that are ready for adoption
            print(pet_list[i].sanctuaryid)

# Creates the list of cats ready for adoption
def cat_list():
    print("\n" + "Cats ready for adoption:")
    for i in range(0, len(pet_list) - 1):
        if pet_list[i].type == "Cat" and pet_list[i].vaccinated == "Yes" and pet_list[i].neutered == "Yes" \
                and pet_list[i].micro != "":
            # Prints out the list of cat ID's that are ready for adoption
            print(pet_list[i].sanctuaryid)


def return_to_owner():
    # Creates a new list to hold the information in. Combining information of both pets and wild animals
    returnList = []
    # Loops through both wild and pet list to find animals i consider ready to return to their owner
    for i in range(0, len(pet_list) - 1):
        if pet_list[i].admission == "Lost" or pet_list[i].admission == "Car Accident":
            returnList.append(pet_list[i].sanctuaryid)
    for j in range(0, len(wild_list) - 1):
        if wild_list[j].admission == "Car Accident":
            returnList.append(wild_list[j].sanctuaryid)
    print("List of animals ready to be returned to their owners: ")
    # Calls the sort algorithm to put them in ascending order
    bubble_sort(returnList)

# Creates the list of owneres who have abandoned animals
def abandon_owner():
    # Lists to hold values in order for us to only filter unique ones
    place_list = []
    abandon_list = []
    # Searches for all owners who has abandoned animals in the past
    for i in range(0, len(treatment_list) - 1):
        if treatment_list[i].abandon != "":
            # Adds names to the temp list
            place_list.append(treatment_list[i].abandon)
    for unique in place_list:
        # Adds all of the names that have not appeared before to the new list
        if unique not in abandon_list:
            abandon_list.append(unique)
    print("List of People who have abused animals:")
    # Sorts list of names by alphabetical order
    bubble_sort(abandon_list)

# Creates the list of owneres who have abused animals
def abuse_owner():
    # Lists to hold values in order for us to only filter unique ones
    holder_list = []
    abuse_list = []
    for i in range(0, len(treatment_list) - 1):
        # Adds names to the temp list
        if treatment_list[i].abuse != "":
            holder_list.append(treatment_list[i].abuse)
    for unique in holder_list:
        if unique not in abuse_list:
            abuse_list.append(unique)
    print("List of People who have abused animals:")
    bubble_sort(abuse_list)

# Starts the program up
menu()

