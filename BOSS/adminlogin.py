from flask import Flask, render_template, request, redirect, url_for, send_file, flash, session
from database_connector import DatabaseConnector
from read import Read

read_instance = Read(DatabaseConnector(host="localhost", user="root", passwd="", database="barangay_official"))

def adminlogin():
    if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            print(f"Attempting login for username: {username}")

            admin_info = read_instance.read_admininfo(username)
            user_info = read_instance.read_userinfo(username, password)

            if admin_info:
                print("Admin account found")
                if password == admin_info[0][5]:
                    print("Admin password matched")
                    session['username'] = username
                    session['admin_info'] = admin_info[0]
                    return render_template('Admin/Home/adminhome.html')
            elif user_info:
                print("User account found")
                if password == user_info[0][2]:
                    print("User password matched")
                    session['username'] = username
                    session['user_info'] = user_info[0]
                    return render_template('#userhome.html')

            print("Invalid username or password")
            return render_template('Admin/login.html', error='Invalid username or password')

    return render_template('Admin/login.html')