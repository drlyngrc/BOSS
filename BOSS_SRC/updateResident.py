from flask import render_template, session, redirect, request, url_for
from connection import DatabaseConnection

class UpdateResident:
    def __init__(self):
        self.db_connector = DatabaseConnection()

    def process_update(self, form_data):
        if 'barangayid' not in session:
            return redirect(url_for('login_route'))

        connection = self.db_connector.get_connection()
        cursor = connection.cursor()

        registration_status = None
        barangayid = session['barangayid']

        try:
            email = form_data.get('email')
            birthplace = form_data.get('birthplace')
            citizenship = form_data.get('citizenship')
            religion = form_data.get('religion')
            civilstat = form_data.get('civilstat')
            contactno = form_data.get('contactno')
            zone = form_data.get('zone')
            streetname = form_data.get('streetname')
            city = form_data.get('city')
            province = form_data.get('province')
            category = form_data.get('selectedOption')
            householdno = form_data.get('householdno')

            # Update Resident Info
            query2 = "UPDATE residentinfo SET birthplace=%s, citizenship=%s, religion=%s, civilstat=%s, contactno=%s WHERE barangayid=%s"
            values2 = (birthplace, citizenship, religion, civilstat, contactno, barangayid)
            cursor.execute(query2, values2)

            # Update Login Info
            query1 = "UPDATE logininfo SET email=%s WHERE barangayid=%s"
            values1 = (email, barangayid)
            cursor.execute(query1, values1)

            # Update Address Info
            query3 = "UPDATE addressinfo SET householdno=%s, zone=%s, streetname=%s, city=%s, province=%s WHERE barangayid=%s"
            values3 = (householdno, zone, streetname, city, province, barangayid)
            cursor.execute(query3, values3)

            if category == "student":
                # Update Student Info
                query4 = "UPDATE studentinfo SET yearlevel=%s, schoolenrolledto=%s, academicyear=%s, scholarship=%s WHERE barangayid=%s"
                values4 = (
                    form_data.get('yearlevel'),
                    form_data.get('schoolenrolledto'),
                    form_data.get('academicyear'),
                    form_data.get('scholarship'),
                    barangayid,
                )
                cursor.execute(query4, values4)

            elif category == "adult":
                # Update Adult Info
                query5 = "UPDATE adultinfo SET employmentstatus=%s, monthlyincome=%s WHERE barangayid=%s"
                values5 = (form_data.get('employmentstatus'), form_data.get('monthlyincome'), barangayid)
                cursor.execute(query5, values5)

            # Commit the changes using the connection, not 'db'
            connection.commit()
            registration_status = "Update successful"

        except Exception as e:
            # Handle any exceptions or errors that may occur during the database operation
            connection.rollback()
            print(f"Error: {str(e)}")
            registration_status = f"Failed to update the record: {str(e)}"

        finally:
            # Close the cursor and database connection
            cursor.close()
            connection.close()

        print(f"Update Status: {registration_status}")

        return render_template("Residents/Update/update.html", registration_status=registration_status, barangayid=barangayid)

    def handle_update_request(self):
        if request.method == 'POST':
            form_data = request.form
            return self.process_update(form_data)
        else:
            # Handle the GET request (if needed)
            barangayid = session.get('barangayid', None)
            return render_template("Residents/Update/update.html", barangayid=barangayid)