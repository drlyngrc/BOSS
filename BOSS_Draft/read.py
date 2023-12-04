from database_connector import DatabaseConnector

class Read(DatabaseConnector):
    def __init__(self, db_connector):
        self.db_connector = db_connector
        self.mycursor = db_connector.get_cursor()
        
    def read_residentinfo(self):
        query = "SELECT * FROM residentinfo"
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results

    def read_medicalinfo(self):
        query = """
                SELECT ri.LastName, ri.FirstName, ri.MiddleName, ri.Sex, ri.Birthdate, mi.* 
                FROM MedicalInfo mi JOIN ResidentInfo ri ON mi.BarangayID = ri.BarangayID 
                """      
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results
    
    def read_caseinfo(self):
        query = """
                SELECT ri.LastName, ri.FirstName, ri.MiddleName, ci.*
                FROM ResidentInfo ri JOIN CaseInfo ci ON ri.BarangayID = ci.BID
                """
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results
    
    def read_addressinfo(self):
        query = "SELECT * FROM addressinfo"
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results
    
    def read_adultinfo(self):
        query = "SELECT * FROM adultinfo"
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results
    
    def read_studentinfo(self):
        query = "SELECT * FROM studentinfo"
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results
    
    def read_householdinfo(self, householdno):
        query = """
                SELECT adrs.HouseholdNo, ri.LastName, ri.FirstName, ri.MiddleName
                FROM ResidentInfo ri
                JOIN AddressInfo adrs ON ri.BarangayID = adrs.BarangayID
                WHERE adrs.HouseholdNo = %s
                """
        values = (householdno,)
        self.mycursor.execute(query, values)
        results = self.mycursor.fetchall()
        return results
    
    def read_incomerecord(self, householdno):
        query = """
                SELECT adrs.HouseholdNo, SUM(ai.MonthlyIncome) AS CombinedIncome
                FROM AddressInfo adrs
                JOIN AdultInfo ai ON adrs.BarangayID = ai.BarangayID
                WHERE adrs.HouseholdNo = %s
                GROUP BY adrs.HouseholdNo
                """
        # Values should be a tuple
        values = (householdno,)
        self.mycursor.execute(query, values)
        results = self.mycursor.fetchall()
        return results

    def read_unemploymentinfo(self):
        query = """
                SELECT ri.BarangayID, ri.LastName, ri.FirstName, ri.MiddleName, ai.EmploymentStatus
                FROM ResidentInfo ri
                JOIN AdultInfo ai ON ri.BarangayID = ai.BarangayID
                WHERE ai.EmploymentStatus = 'Unemployed'

                """
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results

    def read_scholarshipinfo(self):
        query = """
                SELECT ri.BarangayID, ri.LastName, ri.FirstName, ri.MiddleName, si.Scholarship
                FROM ResidentInfo ri
                JOIN StudentInfo si ON ri.BarangayID = si.BarangayID
                WHERE si.Scholarship IS NOT NULL
                """
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results

    def read_admininfo(self, username):
        query = """
                SELECT * FROM AdminInfo WHERE AdminID = %s
                """
        values = (username,)
        self.mycursor.execute(query, values)
        results = self.mycursor.fetchall()
        return results

    def read_userinfo(self, username):
        query = """
                SELECT * FROM LoginInfo WHERE BarangayID = %s
                """
        values = (username,)
        self.mycursor.execute(query, values)
        results = self.mycursor.fetchall()
        return results

    def read_appointment(self):
        query = """
                SELECT
                    a.appointmentid,
                    r.LastName,
                    r.FirstName,
                    r.MiddleName,
                    a.BarangayID,
                    a.Purpose,
                    a.date,
                    a.status
                FROM
                    appointment a
                JOIN
                    residentinfo r ON a.BarangayID = r.BarangayID
                """
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results
