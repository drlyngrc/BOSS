from flask import Flask, render_template, request, redirect, url_for

class Adult:
    def __init__(self, read_instance, delete_instance, update_instance):
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def adultinfo(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "delete":
                    employeeid = request.form["deleteemployeeid"]
                    self.delete_instance.delete_adultinfo(employeeid)
                elif request.form["action"] == "edit":
                    editemployeeid = request.form["editemployeeid"]
                    editemploymentstatus = request.form["editemploymentstatus"]
                    editmonthlyincome = request.form["editmonthlyincome"]

                    return redirect(url_for("updateAdultInfo_route", editemployeeid=editemployeeid,
                                            editemploymentstatus=editemploymentstatus,
                                            editmonthlyincome=editmonthlyincome))

        adultinfo = self.read_instance.read_adultinfo()
        return render_template("adultinfo.html", adultinfo=adultinfo)

    def updateAdultInfo(self, request):
        if request.method == "POST":
            updateemployeeid = request.form["updateemployeeid"]
            updateemploymentstatus = request.form["updateemploymentstatus"]
            updatemonthlyincome = request.form["updatemonthlyincome"]

            self.update_instance.update_adultinfo(updateemployeeid, updateemploymentstatus, updatemonthlyincome)
            return redirect("/adultinfo")

        editemployeeid = request.args.get("editemployeeid")
        editemploymentstatus = request.args.get("editemploymentstatus")
        editmonthlyincome = request.args.get("editmonthlyincome")

        return render_template("updateAdult.html", editemployeeid=editemployeeid,
                               editemploymentstatus=editemploymentstatus,
                               editmonthlyincome=editmonthlyincome)
