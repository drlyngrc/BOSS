from database_connector import DatabaseConnector

class Create:
    def __init__(self, db_connector):
        self.db = db_connector

    def create_residentinfo(self, barangayid, category, lastname, firstname, middlename, sex, 
                            birthdate, birthplace, religion, civilstat, citizenship, voterprecinct, contactno, profile_picture):
        query = "INSERT INTO residentinfo VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (barangayid, category, lastname, firstname, middlename, sex, birthdate, 
                  birthplace, religion, civilstat, citizenship, voterprecinct, contactno, profile_picture) 
        self.db.execute_query(query, values)
        self.db.commit()

    def create_addressinfo(self, barangayid, householdno, zone, streetname, city, province):
        query = "INSERT INTO addressinfo VALUES ('', '', %s, %s, %s, %s, %s, %s)"
        values = (barangayid, householdno, zone, streetname, city, province)
        self.db.execute_query(query, values)
        self.db.commit()

    def create_medicalinfo(self, barangayid, bmiclassification, medicalcondition, covidvaccinated, maintenancemedicine, physicalfitness):
        query = "INSERT INTO medicalinfo VALUES ('', '', %s, %s, %s, %s, %s, %s)"
        values = (barangayid, bmiclassification, medicalcondition, covidvaccinated, maintenancemedicine, physicalfitness)
        self.db.execute_query(query, values)
        self.db.commit()

    def create_caseinfo(self, bid, casedesc, casestatus):
        query = "INSERT INTO caseinfo VALUES ('', '', %s, %s, %s)"
        values = (bid, casedesc, casestatus)
        self.db.execute_query(query, values)
        self.db.commit()

    def create_adultinfo(self, barangayid, employmentstatus, monthlyincome):
        query = "INSERT INTO adultinfo VALUES ('', '', %s, %s, %s)"
        values = (barangayid, employmentstatus, monthlyincome)
        self.db.execute_query(query, values)
        self.db.commit()

    def create_studentinfo(self, barangayid, yearlevel, school, academicyear, scholarship):
        query = "INSERT INTO studentinfo VALUES ('', '', %s, %s, %s, %s, %s)"
        values = (barangayid, yearlevel, school, academicyear, scholarship)
        self.db.execute_query(query, values)
        self.db.commit()

    def create_logininfo(self, barangayid, password, email):
        query = "INSERT INTO logininfo VALUES ('', %s, %s, %s)"
        values = (barangayid, password, email)
        self.db.execute_query(query, values)
        self.db.commit()

    def create_uploadfile(self, id, filename, filepath):
        query = "INSERT INTO files (filename, filepath) VALUES (%s, %s)"
        values = (filename, filepath)
        self.db.execute_query(query, values)
        self.db.commit()
