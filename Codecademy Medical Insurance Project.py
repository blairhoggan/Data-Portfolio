import csv

ages = []
sexes = []
bmis = []
children = []
smoker = []
regions = []
charges = []

def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csvDict = csv.DictReader(csv_info)
        for row in csvDict:
            lst.append(row[column_name])
        return lst

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(children, 'insurance.csv', 'children')
load_list_data(smoker, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(charges, 'insurance.csv', 'charges')

class PatientsInfo:
    # init method that takes in each list parameter
    def __init__(self, patients_ages, patients_sexes, patients_bmis,
                 patients_children, patients_smoker, patients_region,
                 patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_children = patients_children
        self.patients_smoker = patients_smoker
        self.patients_region = patients_region
        self.patients_charges = patients_charges

    # method that calculates the average age of a patient
    def analyse_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return ("Average patient age " +
                str(round(total_age/len(self.patients_ages), 2)) + " years")

    # method that counts the number of male and female patients
    def  analyse_sexes(self):
        females = 0
        males = 0
        for sex in self.patients_sexes:
            if sex == 'female':
                females += 1
            else:
                males += 1
        print("Count for female: ", females)
        print("Count for male: ", males)

    # method to find each unique region patients are from
    def analyse_regions(self):
        unique_regions = []
        for region in self.patients_region:
            if region not in regions:
                unique_regions.append(region)
        return unique_regions

    # method to find average yearly medical charges for patients in insurance.csv
    def average_charges(self):
        total_charge = 0
        for charge in self.patients_charges:
            total_charge += float(charge)
        return ("Average charge for patients is " +
                str(round(total_charge/len(self.patients_charges), 2))
                + " dollars.")

    # method to create dictionary with all patients info
    def create_dict(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_children
        self.patients_dictionary["smoker"] = self.patients_smoker
        self.patients_dictionary["regions"] = self.patients_region
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary


'''create instance of the class.
We can use each method to see the results of the analysis'''

patient_info = PatientsInfo(ages, sexes, bmis, children,
                            smoker, regions, charges)

patient_info.create_dict()




        








        










        





    
        
