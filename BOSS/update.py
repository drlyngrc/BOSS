from database_connector import DatabaseConnector

class Update:
    def __init__(self, db_connector):
        self.db = db_connector

    def update_residentinfo(self, barangayid, category, lastname, firstname, middlename, sex, 
                            birthdate, birthplace, religion, civilstat, citizenship, voterprecinct, contactno):
        query = """
        UPDATE ResidentInfo
        SET 
            Category = %s,
            LastName = %s,
            FirstName = %s,
            MiddleName = %s,
            Sex = %s,
            BirthDate = %s,
            BirthPlace = %s,
            Religion = %s,
            CivilStat = %s,
            Citizenship = %s,
            VoterPrecinct = %s,
            ContactNo = %s
        WHERE BarangayID = %s
        """
        values = (category, lastname, firstname, middlename, sex, birthdate, birthplace,
                  religion, civilstat, citizenship, voterprecinct, contactno, barangayid)
        self.db.execute_query(query, values)
        self.db.commit()

    def update_medicalinfo(self, medicalid, bmiclassification, medicalcondition, covidvaccinated, maintenancemedicine, physicalfitness):
        query = """ 
                UPDATE MedicalInfo
                SET
                    BMIClassification = %s,
                    MedicalCondition = %s,
                    COVIDVaccinated = %s,
                    MaintenanceMedicine = %s,
                    PhysicalFitness = %s
                WHERE MedicalID = %s
                """
        values = (bmiclassification, medicalcondition, covidvaccinated, maintenancemedicine, physicalfitness, medicalid)
        self.db.execute_query(query, values)
        self.db.commit()

    def update_addressinfo(self, addressid, householdno, zone, streetname, city, province):
        query = """
                UPDATE AddressInfo
                SET 
                    HouseholdNo = %s,
                    Zone = %s,
                    StreetName = %s,
                    City = %s,
                    Province = %s
                WHERE AddressID = %s
                """
        values = (householdno, zone, streetname, city, province, addressid)
        self.db.execute_query(query, values)
        self.db.commit()

    def update_caseinfo(self, caseid, casedesc, casestatus):
        query = """
                UPDATE CaseInfo 
                SET 
                    CaseDesc = %s,
                    CaseStatus = %s
                WHERE CaseID = %s
                """
        values = (casedesc, casestatus, caseid)
        self.db.execute_query(query, values)
        self.db.commit()

    def update_adultinfo(self, employeeid, employmentstatus, monthlyincome):
        query = """
                UPDATE AdultInfo
                SET 
                    EmploymentStatus = %s,
                    MonthlyIncome = %s
                WHERE EmployeeID = %s
                """
        values = (employmentstatus, monthlyincome, employeeid)
        self.db.execute_query(query, values)
        self.db.commit()

    def update_studentinfo(self, studentid, yearlevel, school, academicyear, scholarship):
        query = """
                UPDATE StudentInfo
                SET
                    YearLevel = %s,
                    School = %s,
                    AcademicYear = %s,
                    Scholarship = %s
                WHERE StudentID = %s
                """
        values = (yearlevel, school, academicyear, scholarship, studentid)
        self.db.execute_query(query, values)
        self.db.commit()

    def update_appointment(self, appointmentid, status):
        query = """
                UPDATE appointment
                SET 
                    Status = %s
                WHERE appointmentid = %s
                """
        values = (status, appointmentid)
        self.db.execute_query(query, values)
        self.db.commit()



