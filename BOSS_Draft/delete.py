from database_connector import DatabaseConnector

class Delete:
    def __init__(self, db_connector):
        self.db = db_connector

    def delete_residentinfo(self, barangayid):
        query = "DELETE FROM residentinfo WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_medicalinfo(self, medicalid):
        query = "DELETE FROM medicalinfo WHERE MedicalID = %s"
        value = (medicalid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_caseinfo(self, caseid):
        query = "DELETE FROM caseinfo WHERE CaseID = %s"
        value = (caseid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_addressinfo(self, addressid):
        query = "DELETE FROm addressinfo WHERE AddressID = %s"
        value = (addressid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_adultinfo(self, adultid):
        query = "DELETE FROM adultinfo WHERE EmployeeID = %s"
        value = (adultid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_studentinfo(self, studentid):
        query = "DELETE FROM studentinfo WHERE StudentID = %s"
        value = (studentid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_appointment(self, appointmentid):
        query = "DELETE FROM appointment WHERE appointmentid = %s"
        value = (appointmentid,)
        self.db.execute_query(query, value)
        self.db.commit()

    
