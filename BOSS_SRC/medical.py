from flask import request, render_template, redirect, url_for, session, g
from connection import DatabaseConnection

class MedicalResident:
    def __init__(self):
        self.db_connector = DatabaseConnection()

    def get_db(self):
        if 'db' not in g:
            g.db = self.db_connector.get_connection()
        return g.db

    def close_db(self, exception=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    def process_medical(self):
        registration_status = None

        # Check if 'barangayid' is in the session
        if 'barangayid' not in session:
            return redirect(url_for('login_route'))

        connection = self.get_db()
        cursor = connection.cursor()

        # Initialize barangayid with a default value
        barangayid = session['barangayid']

        if request.method == 'POST':
            try:
                # Correct way to get data from the form
                bmi_classification = request.form.get('bmi_classification')
                medical_condition = request.form.get('medical_condition')
                covid_vaccinated = request.form.get('covid_vaccinated')
                maintenance_medicine = request.form.get('maintenance_medicine')
                physical_fitness = request.form.get('physical_fitness')

                # Update Resident Info
                # Insert Medical Info
                query = "INSERT INTO medicalinfo (BMIClassification, MedicalCondition, CovidVaccinated, MaintenanceMedicine, PhysicalFitness, barangayid) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (bmi_classification, medical_condition, covid_vaccinated, maintenance_medicine, physical_fitness, barangayid)
                cursor.execute(query, values)

                # Commit the changes using the connection, not 'db'
                connection.commit()
                registration_status = "Update successful"

            except Exception as e:
                # Handle any exceptions or errors that may occur during the database operation
                connection.rollback()
                print(f"Error: {str(e)}")
                registration_status = f"Failed to update the record: {str(e)}"

            finally:
                # Close the cursor (no need to close the connection explicitly)
                cursor.close()

        print(f"Update Status: {registration_status}")

        return render_template('Residents/Dashboard/Medical/medical.html', registration_status=registration_status, barangayid=barangayid)
