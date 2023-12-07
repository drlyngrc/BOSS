from flask import request, render_template, redirect, url_for, session
from read import Read
from database_connector import DatabaseConnector

# Assuming your DatabaseConnector class is initialized here
read_instance = Read(DatabaseConnector(host="localhost", user="root", passwd="", database="barangay_official"))

def Login():
    if request.method == 'POST':
        barangayid = request.form.get('barangayid')
        password = request.form.get('password')
        session['barangayid'] = barangayid

        # Check credentials against the database using read_userinfo method
        user = read_instance.read_userinfo(barangayid, password)

        print("user:", user)  # Add this line for debugging

        if user and user['Password'] == password:
            # If user exists and password is correct, render the dashboard
            return redirect(url_for('dashboard_route'))
        else:
            # If credentials are incorrect, render an error message
            print("Incorrect password. Password entered:", password)  # Add this line for debugging
            return render_template('Residents/index.html', error="Incorrect password.")

    # If the request method is GET, render the login page
    return render_template('Residents/index.html')