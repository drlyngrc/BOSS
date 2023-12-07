# app.py
# Resident
from flask import Flask, render_template, request, redirect, url_for, send_file, flash, session
from connection import DatabaseConnection
from login import Login
from dashboard import DashboardManager
from appointment import AppointmentResident
from updateResident import UpdateResident
from medical import MedicalResident

# Admin
import os
from create import Create
from read import Read
from update import Update, ResidentInfoUpdater
from delete import Delete
from database_connector import DatabaseConnector
from werkzeug.utils import secure_filename
from package.case import CaseManager
from package.resident import ResidentManager
from package.medical import MedicalManager
from package.address import AddressManager
from package.adult import AdultManager
from package.student import StudentManager
from package.derived_tables import DerivedTablesManager
from package.appointment import AppointmentManager
from adminregistration import adminregistration
from adminlogin import adminlogin

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secretsecret'

# Instantiate the DatabaseConnector class

db_connection = DatabaseConnection()
# Instantiate the Login, Dashboard, Appointment, Update, and Medical classes
db_connector = DatabaseConnector(host="localhost", user="root", passwd="", database="barangay_official")
create_instance = Create(db_connector)
read_instance = Read(db_connector)
update_instance = Update(db_connector)
delete_instance = Delete(db_connector)
resident_updater = ResidentInfoUpdater(db_connector)

case_instance = CaseManager(create_instance, read_instance, delete_instance, update_instance, resident_updater)
resident_instance = ResidentManager(read_instance, delete_instance, update_instance, resident_updater)
medical_instance = MedicalManager(read_instance, delete_instance, update_instance, resident_updater)
address_instance = AddressManager(read_instance, delete_instance, update_instance, resident_updater)
adult_instance = AdultManager(read_instance, delete_instance, update_instance, resident_updater)
student_instance = StudentManager(read_instance, delete_instance, update_instance, resident_updater)
derived_tables_instance = DerivedTablesManager(read_instance)
appointment_instance = AppointmentManager(read_instance, delete_instance, update_instance, resident_updater)

dashboard_instance = DashboardManager()
appointment_instance_resident = AppointmentResident(db_connection)
update_instance_resident = UpdateResident()
medical_instance_resident = MedicalResident()

# Resident Page
@app.route('/', methods=['GET', 'POST'])
def login_route():
    return Login()

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard_route():
    return dashboard_instance.dashboard()

@app.route('/dashboard/appointment', methods=['GET', 'POST'])
def appointment_route():
    return appointment_instance_resident.process_appointment()

@app.route('/dashboard/update', methods=['GET', 'POST'])
def update_route():
    response = update_instance_resident.handle_update_request()
    return response  # Make sure to return a valid response

@app.route('/dashboard/medical', methods=['GET', 'POST'])
def medical_route():
    return medical_instance_resident.process_medical()

@app.route('/dashboard/appointment', methods=['GET', 'POST'])
def process_appointment():
    appointment_instance = AppointmentResident(db_connector)
    return appointment_instance.process_appointment()

# Log out
@app.route('/logout', methods=['POST'])
def logout():
    print("Before Logout:", session)
    session.pop('barangayid', None)
    print("After Logout:", session)
    return redirect(url_for('login_route'))



# Admin
def save_file(file):
    upload_folder = "uploads"

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filename = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(filename)
    return filename

@app.route("/admin")
def home():
    return render_template("/Admin/Home/adminhome.html")

@app.route("/admin/appointment", methods=["GET", "POST"])
def appointment():
    return appointment_instance.appointment(request)

@app.route("/admin/updateAppointment", methods=["GET", "POST"])
def updateAppointment():
    return appointment_instance.updateAppointment(request)

@app.route("/admin/residentinfo", methods=["GET", "POST"])
def residentinfo_route():
    return resident_instance.residentinfo(request)

@app.route("/admin/updateResidentInfo", methods=["GET", "POST"])
def updateResidentInfo_route():
    return resident_instance.updateResidentInfo(request)

@app.route("/admin/medicalinfo", methods=["GET", "POST"])
def medicalinfo_route():
    return medical_instance.medicalinfo(request)

@app.route("/admin/updateMedicalInfo", methods=["GET", "POST"])
def updateMedicalInfo_route():
    return medical_instance.updateMedicalInfo(request)

@app.route("/admin/addressinfo", methods=["GET", "POST"])
def addressinfo_route():
    return address_instance.addressinfo(request)

@app.route("/admin/updateAddressInfo", methods=["GET", "POST"])
def updateAddressInfo_route():
    return address_instance.updateAddressInfo(request)

@app.route("/admin/caseinfo", methods=["GET", "POST"])
def caseinfo_route():
    return case_instance.caseinfo(request)

@app.route("/admin/updateCaseInfo", methods=["GET", "POST"])
def updateCaseInfo_route():
    return case_instance.updateCaseInfo(request)

@app.route("/admin/adultinfo", methods=["GET", "POST"])
def adultinfo_route():
    return adult_instance.adultinfo(request)

@app.route("/admin/updateAdultInfo", methods=["GET", "POST"])
def updateAdultInfo_route():
    return adult_instance.updateAdultInfo(request)

@app.route("/admin/studentinfo", methods=["GET", "POST"])
def studentinfo_route():
    return student_instance.studentinfo(request)

@app.route("/admin/updateStudentInfo", methods=["GET", "POST"])
def updateStudentInfo_route():
    return student_instance.updateStudentInfo(request)

@app.route("/admin/householdinfo", methods=["GET", "POST"])
def householdinfo_route():
    return derived_tables_instance.householdinfo(request)

@app.route("/admin/incomerecord", methods=["GET", "POST"])
def incomerecord_route():
    return derived_tables_instance.incomerecord(request)

@app.route("/admin/unemploymentinfo", methods=["GET", "POST"])
def unemploymentinfo_route():
    return derived_tables_instance.unemploymentinfo()

@app.route("/admin/scholarshipinfo", methods=["GET", "POST"])
def scholarshipinfo_route():
    return derived_tables_instance.scholarshipinfo()

@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    return adminlogin()

@app.route("/admin/registration", methods=["GET", "POST"])
def accregistration():
    return adminregistration()

if __name__ == '__main__':
    app.run(debug=True)
