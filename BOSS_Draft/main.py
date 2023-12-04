# main.py

import os
from flask import Flask, render_template, request, redirect, url_for, send_file, flash, session
from create import Create
from read import Read
from update import Update
from delete import Delete
from database_connector import DatabaseConnector
from werkzeug.utils import secure_filename
from package.case import Case
from package.resident import Resident
from package.medical import Medical
from package.address import Address
from package.adult import Adult
from package.student import Student
from package.derived_tables import DerivedTables
from package.appointment import Appointment


app = Flask(__name__)
app.secret_key = 'BOSS'

db_connector = DatabaseConnector(host="localhost", user="root", passwd="", database="Barangay")
create_instance = Create(db_connector)
read_instance = Read(db_connector)
update_instance = Update(db_connector)
delete_instance = Delete(db_connector)

case_instance = Case(create_instance, read_instance, delete_instance, update_instance)
resident_instance = Resident(read_instance, delete_instance, update_instance)
medical_instance = Medical(read_instance, delete_instance, update_instance)
address_instance = Address(read_instance, delete_instance, update_instance)
adult_instance = Adult(read_instance, delete_instance, update_instance)
student_instance = Student(read_instance, delete_instance, update_instance)
derived_tables_instance = DerivedTables(read_instance)
appointment_instance = Appointment(read_instance, delete_instance, update_instance)


def save_file(file):
    upload_folder = "uploads"

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filename = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(filename)
    return filename

@app.route("/admin")
def home():
    return render_template("Home/adminhome.html")

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    return appointment_instance.appointment(request)

@app.route("/updateAppointment", methods=["GET", "POST"])
def updateAppointment():
    return appointment_instance.updateAppointment(request)

@app.route("/residentinfo", methods=["GET", "POST"])
def residentinfo_route():
    return resident_instance.residentinfo(request)

@app.route("/updateResidentInfo", methods=["GET", "POST"])
def updateResidentInfo_route():
    return resident_instance.updateResidentInfo(request)

@app.route("/medicalinfo", methods=["GET", "POST"])
def medicalinfo_route():
    return medical_instance.medicalinfo(request)

@app.route("/updateMedicalInfo", methods=["GET", "POST"])
def updateMedicalInfo_route():
    return medical_instance.updateMedicalInfo(request)

@app.route("/addressinfo", methods=["GET", "POST"])
def addressinfo_route():
    return address_instance.addressinfo(request)

@app.route("/updateAddressInfo", methods=["GET", "POST"])
def updateAddressInfo_route():
    return address_instance.updateAddressInfo(request)

@app.route("/caseinfo", methods=["GET", "POST"])
def caseinfo_route():
    return case_instance.caseinfo(request)

@app.route("/updateCaseInfo", methods=["GET", "POST"])
def updateCaseInfo_route():
    return case_instance.updateCaseInfo(request)

@app.route("/adultinfo", methods=["GET", "POST"])
def adultinfo_route():
    return adult_instance.adultinfo(request)

@app.route("/updateAdultInfo", methods=["GET", "POST"])
def updateAdultInfo_route():
    return adult_instance.updateAdultInfo(request)

@app.route("/studentinfo", methods=["GET", "POST"])
def studentinfo_route():
    return student_instance.studentinfo(request)

@app.route("/updateStudentInfo", methods=["GET", "POST"])
def updateStudentInfo_route():
    return student_instance.updateStudentInfo(request)

@app.route("/householdinfo", methods=["GET", "POST"])
def householdinfo_route():
    return derived_tables_instance.householdinfo(request)

@app.route("/incomerecord", methods=["GET", "POST"])
def incomerecord_route():
    return derived_tables_instance.incomerecord(request)

@app.route("/unemploymentinfo", methods=["GET", "POST"])
def unemploymentinfo_route():
    return derived_tables_instance.unemploymentinfo()

@app.route("/scholarshipinfo", methods=["GET", "POST"])
def scholarshipinfo_route():
    return derived_tables_instance.scholarshipinfo()

###############################################################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(f"Attempting login for username: {username}")

        admin_info = read_instance.read_admininfo(username)
        user_info = read_instance.read_userinfo(username)

        if admin_info:
            print("Admin account found")
            if password == admin_info[0][5]:
                print("Admin password matched")
                session['username'] = username
                session['admin_info'] = admin_info[0]
                return render_template('Home/adminhome.html')
        elif user_info:
            print("User account found")
            if password == user_info[0][2]:
                print("User password matched")
                session['username'] = username
                session['user_info'] = user_info[0]
                return render_template('#userhome.html')

        print("Invalid username or password")
        return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


###############################################################################################

@app.route("/accregistration", methods=["GET", "POST"])
def accregistration():
    print(request.form)
    if request.method == "POST":
        if "action" in request.form:
            if request.form["action"] == "create":
                barangayid = request.form["barangayid"]
                category = request.form["category"]
                lastname = request.form["lastname"]
                firstname = request.form["firstname"]
                middlename = request.form["middlename"]
                sex = request.form["sex"]
                birthdate = request.form["birthdate"]
                birthplace = request.form["birthplace"]
                religion = request.form["religion"]
                civilstat = request.form["civilstat"]
                citizenship = request.form["citizenship"]
                voterprecinct = request.form["voterprecinct"]
                contactno = request.form["contactno"]
                employmentstatus = request.form["employmentstatus"]
                monthlyincome = request.form["monthlyincome"]
                yearlevel = request.form["yearlevel"]
                school = request.form["school"]
                academicyear = request.form["academicyear"]
                scholarship = request.form["scholarship"]
                houseno = request.form["houseno"]
                zone = request.form["zone"]
                streetname = request.form["streetname"]
                city = request.form["city"]
                province = request.form["province"]
                bmiclassification = request.form["bmiclassification"]
                medicalcondition = request.form["medicalcondition"]
                covidvaccinated = request.form["covidvaccinated"]
                maintenancemedicine = request.form["maintenancemedicine"]
                physicalfitness = request.form["physicalfitness"]
                profile_picture = request.files['profile_picture']
                saved_filepath = save_file(profile_picture)
                if saved_filepath:
                    create_instance.create_residentinfo(barangayid, category, lastname, firstname, middlename, sex, birthdate,
                                                        birthplace, religion, civilstat, citizenship, voterprecinct, contactno,
                                                        saved_filepath)

                # Create instances for addressinfo, medicalinfo, adultinfo, studentinfo based on the selected category
                if category == "Adult":
                    create_instance.create_adultinfo(request.form["adult_barangayid"], employmentstatus, monthlyincome)
                    create_instance.create_addressinfo(request.form["address_barangayid"], houseno, zone, streetname, city, province)
                    create_instance.create_medicalinfo(request.form["medical_barangayid"], bmiclassification, medicalcondition, covidvaccinated, 
                                                    maintenancemedicine, physicalfitness)

                elif category == "Student":
                    create_instance.create_studentinfo(request.form["student_barangayid"], yearlevel, school, academicyear, scholarship)
                    create_instance.create_addressinfo(request.form["address_barangayid"], houseno, zone, streetname, city, province)
                    create_instance.create_medicalinfo(request.form["medical_barangayid"], bmiclassification, medicalcondition, covidvaccinated, 
                                                    maintenancemedicine, physicalfitness)
                elif category == "Others":
                    create_instance.create_addressinfo(request.form["address_barangayid"], houseno, zone, streetname, city, province)
                    create_instance.create_medicalinfo(request.form["medical_barangayid"], bmiclassification, medicalcondition, covidvaccinated, 
                                                    maintenancemedicine, physicalfitness)

                
                return redirect(url_for('accregistration'))

    return render_template("Info/accregistration.html", accregistration=accregistration)

###############################################################################################

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'

        if file:
            upload_folder = "uploads"
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            filename = os.path.join(upload_folder, secure_filename(file.filename))
            file.save(filename)
            filepath = filename

            id = request.form.get('id')
            create_instance.create_uploadfile(id, filename, filepath)
            return 'File uploaded successfully!'

    return render_template("File/uploadfile.html")
@app.route("/upload_request_form")
def upload_request_form():
    return render_template("Home/adminhome.html")
@app.route("/upload_form")
def upload_form():
    return render_template("File/uploadfile.html")

###############################################################################################

#downloads
@app.route('/download')
def user():
    cursor = db_connector.get_cursor()
    cursor.execute("SELECT id, filename FROM files")
    files = cursor.fetchall()
    return render_template('File/downloadfile.html', files=files)

@app.route('/download/<int:file_id>')
def download(file_id):
    cursor = db_connector.get_cursor()
    cursor.execute("SELECT filepath FROM files WHERE id = %s", (file_id,))
    filepath = cursor.fetchone()[0]
    return send_file(filepath, as_attachment=True)

###############################################################################################

if __name__ == '__main__':
    app.run(debug=True)