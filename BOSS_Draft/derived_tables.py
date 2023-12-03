from flask import Flask, render_template, request, redirect, url_for, flash

class DerivedTables:
    def __init__(self, read_instance):
        self.read_instance = read_instance

    def householdinfo(self, request):
        householdno = ''  # Default value for rendering
        householdinfo = []  # Default value for rendering

        if request.method == "POST":
            if "action" in request.form and request.form["action"] == "submit":
                householdno = request.form["householdno"]
                householdinfo = self.read_instance.read_householdinfo(householdno)
                if not householdinfo:
                    flash('No household found for the given number.', 'error')
                return render_template("householdinfo.html", householdinfo=householdinfo)

        return render_template("householdinfo.html", householdinfo=[])

    def incomerecord(self, request):
        householdno = ''
        incomerecord = []  # Default value for rendering

        if request.method == "POST":
            if "action" in request.form and request.form["action"] == "submit":
                householdno = request.form["householdno"]
                incomerecord = self.read_instance.read_incomerecord(householdno)
                if not incomerecord:
                    flash('No records found for the given household number.', 'error')

        return render_template("incomerecord.html", incomerecord=incomerecord)

    def unemploymentinfo(self):
        unemploymentinfo = self.read_instance.read_unemploymentinfo()
        return render_template("unemploymentinfo.html", unemploymentinfo=unemploymentinfo)

    def scholarshipinfo(self):
        scholarshipinfo = self.read_instance.read_scholarshipinfo()
        return render_template("scholarshipinfo.html", scholarshipinfo=scholarshipinfo)
