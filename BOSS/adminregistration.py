from flask import Flask, render_template, request, redirect, url_for, send_file, flash, session
from database_connector import DatabaseConnector
import os
from werkzeug.utils import secure_filename
from create import Create

create_instance = Create(DatabaseConnector(host="localhost", user="root", passwd="", database="barangay_official"))

def save_file(file, barangayid):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    upload_folder = os.path.join(script_directory, 'static', 'uploads', barangayid)

    # Create a directory for the specific barangayid if it doesn't exist
    os.makedirs(upload_folder, exist_ok=True)

    # Save the file to the server in the barangayid directory
    filename = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(filename)

    return filename.replace(os.path.join(script_directory, 'static'), '')  # Save relative path

def adminregistration():
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
                saved_filepath = save_file(profile_picture, barangayid)

                password = request.form["password"]
                email = request.form["email"]
                if saved_filepath:
                    create_instance.create_residentinfo(barangayid, category, lastname, firstname, middlename, sex, birthdate,
                                                        birthplace, religion, civilstat, citizenship, voterprecinct, contactno,
                                                        saved_filepath)
                create_instance.create_logininfo(barangayid, password, email)

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
    return render_template("Admin/Info/accregistration.html")