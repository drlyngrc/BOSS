from flask import Flask, render_template, request, redirect, url_for

class Appointment:
    def __init__(self, read_instance, delete_instance, update_instance):
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def appointment(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "delete":
                    appointmentid = request.form["deleteappointmentid"]
                    self.delete_instance.delete_appointment(appointmentid)
                elif request.form["action"] == "edit":
                    editappointmentid = request.form["editappointmentid"]
                    editstatus = request.form["editstatus"]

                    return redirect(url_for("updateAppointment", editappointmentid=editappointmentid, editstatus=editstatus))

        appointment = self.read_instance.read_appointment()
        return render_template("appointment.html", appointment=appointment)

    def updateAppointment(self, request):
        if request.method == "POST":
            updateappointmentid = request.form["updateappointmentid"]
            updatestatus = request.form["updatestatus"]
    
            self.update_instance.update_appointment(updateappointmentid, updatestatus)
            return redirect("/appointment")

        editappointmentid = request.args.get("editappointmentid")
        editstatus = request.args.get("editstatus")

        return render_template("updateAppointment.html", editappointmentid=editappointmentid, editstatus=editstatus)
