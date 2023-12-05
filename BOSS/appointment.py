from flask import Flask, render_template, request, redirect, url_for, session
from connection import DatabaseConnection

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secret'

class AppointmentResident:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def process_appointment(self):
        if 'barangayid' not in session:
            return redirect(url_for('login_route'))

        connection = self.db_connector.get_connection()
        cursor = connection.cursor()

        appointmentstatus = None  # Initialize the variable
        barangayid = session['barangayid']

        if request.method == 'POST':
            purpose = request.form.get('purpose')
            date = request.form.get('appointmentdate')

            try:
                # Check if an appointment with the given barangayid already exists
                query_check_existing = "SELECT COUNT(*) FROM appointment WHERE barangayid = %s"
                cursor.execute(query_check_existing, (barangayid,))
                existing_count = cursor.fetchone()[0]

                if existing_count > 0:
                    appointmentstatus = "You already have an existing appointment. Only one appointment is allowed."
                else:
                    # Check if the count for the date reaches 5
                    query_count = "SELECT COUNT(*) FROM appointment WHERE date = %s"
                    cursor.execute(query_count, (date,))
                    date_count = cursor.fetchone()[0]

                    if date_count >= 5:
                        appointmentstatus = "This date is no longer available. Please choose another date."
                    else:
                        # Your existing code to insert into the database
                        query_insert = "INSERT INTO appointment (barangayid, purpose, date, status) VALUES (%s, %s, %s, %s)"
                        values_insert = (barangayid, purpose, date, "Pending")
                        cursor.execute(query_insert, values_insert)

                        connection.commit()
                        appointmentstatus = "Wait for the response of an admin"

            except Exception as e:
                # Handle any exceptions or errors that may occur during the database operation
                connection.rollback()
                print(f"Error: {str(e)}")
                appointmentstatus = f"Failed to register the appointment: {str(e)}"

            finally:
                # Close the cursor and database connection
                cursor.close()
                connection.close()

        return render_template("Residents/Dashboard/Appointment/appointment.html", appointmentstatus=appointmentstatus, barangayid=barangayid)

# Route for the process_appointment method
@app.route('/dashboard/appointment', methods=['GET', 'POST'])
def process_appointment():
    appointment_instance = Appointment(db_connector)
    return appointment_instance.process_appointment()

# Note: In a real Flask application, the 'process_appointment' method would be called in response to this route.

if __name__ == '__main__':
    app.run(debug=True)
