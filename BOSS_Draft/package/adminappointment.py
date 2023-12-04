from flask import request, render_template, redirect, url_for

class AdminAppointment:
    def __init__(self, read_instance, delete_instance, update_instance):
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def appointmentStatus(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "delete":
                    appointmentid = request.form["deleteappointmentid"]
                    self.delete_instance.delete_appointment(appointmentid)
                elif request.form["action"] == "edit":
                    editappointmentid = request.form["editappointmentid"]
                    editstatus = request.form["editstatus"]
            
                return redirect(url_for("updateappointment", 
                                        editappointmentid=editappointmentid,
                                        editstatus=editstatus))

        adminappointment = self.read_instance.read_appointment()
        return render_template("adminappointment.html", adminappointment=adminappointment)

    def updateAppointmentStatus(self, request):
        try:
            if request.method == "POST":
                updateappointmentid = request.form["updateappointmentid"]
                updatestatus = request.form["updatestatus"]

                self.update_instance.update_appointmentstatus(updateappointmentid, updatestatus)
                return redirect('/adminappointment')

        except KeyError as e:
            # Handle the KeyError - log the error or take appropriate action
            print("KeyError:", e)

        editappointmentid = request.args.get("editappointmentid")
        editstatus = request.args.get("editstatus")

        return render_template("updateAppointment.html", editappointmentid=editappointmentid, 
                            editstatus=editstatus)

        
    

