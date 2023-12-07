from database_connector import DatabaseConnector

class Delete:
    def __init__(self, db_connector):
        self.db = db_connector

    def delete_residentinfo(self, barangayid):
        # Check for related records and delete them first
        self.delete_related_records(barangayid)

        # Now delete the main residentinfo
        query = "DELETE FROM residentinfo WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_medicalinfo(self, medicalid):
        query = "DELETE FROM medicalinfo WHERE MedicalID = %s"
        value = (medicalid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def del_medicalinfo(self, barangayid):
        query = "DELETE FROM medicalinfo WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_caseinfo(self, caseid):
        query = "DELETE FROM caseinfo WHERE CaseID = %s"
        value = (caseid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def del_caseinfo(self, barangayid):
        query = "DELETE FROM caseinfo WHERE BID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_addressinfo(self, addressid):
        query = "DELETE FROm addressinfo WHERE AddressID = %s"
        value = (addressid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def del_addressinfo(self, barangayid):
        query = "DELETE FROm addressinfo WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_adultinfo(self, adultid):
        query = "DELETE FROM adultinfo WHERE EmployeeID = %s"
        value = (adultid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def del_adultinfo(self, barangayid):
        query = "DELETE FROM adultinfo WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_studentinfo(self, studentid):
        query = "DELETE FROM studentinfo WHERE StudentID = %s"
        value = (studentid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def del_studentinfo(self, barangayid):
        query = "DELETE FROM studentinfo WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_appointment(self, appointmentid):
        query = "DELETE FROM appointment WHERE appointmentid = %s"
        value = (appointmentid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def del_appointment(self, barangayid):
        query = "DELETE FROM appointment WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()
    
    def del_logininfo(self, barangayid):
        query = "DELETE FROM logininfo WHERE BarangayID = %s"
        value = (barangayid,)
        self.db.execute_query(query, value)
        self.db.commit()

    def delete_related_records(self, barangayid):
        # Delete related records in other tables
        self.del_medicalinfo(barangayid)
        self.del_caseinfo(barangayid)
        self.del_addressinfo(barangayid)
        self.del_adultinfo(barangayid)
        self.del_studentinfo(barangayid)
        self.del_appointment(barangayid)
        self.del_logininfo(barangayid)
        # ... delete from other related tables