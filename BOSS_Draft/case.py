from flask import Flask, render_template, request, redirect, url_for

class Case:
    def __init__(self, create_instance, read_instance, delete_instance, update_instance):
        self.create_instance = create_instance
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def caseinfo(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "create":
                    bid = request.form["bid"]
                    casedesc = request.form["casedesc"]
                    casestatus = request.form["casestatus"]
                    self.create_instance.create_caseinfo(bid, casedesc, casestatus)
                elif request.form["action"] == "delete":
                    caseid = request.form["deletecaseid"]
                    self.delete_instance.delete_caseinfo(caseid)
                elif request.form["action"] == "edit":
                    editcaseid = request.form["editcaseid"]
                    editcasedesc = request.form["editcasedesc"]
                    editcasestatus = request.form["editcasestatus"]

                    return redirect(url_for("updateCaseInfo_route", editcaseid=editcaseid, editcasedesc=editcasedesc,
                                            editcasestatus=editcasestatus))

        caseinfo = self.read_instance.read_caseinfo()
        return render_template("caseinfo.html", caseinfo=caseinfo)

    def updateCaseInfo(self, request):
        if request.method == "POST":
            updatecaseid = request.form["updatecaseid"]
            updatecasedesc = request.form["updatecasedesc"]
            updatecasestatus = request.form["updatecasestatus"]

            self.update_instance.update_caseinfo(updatecaseid, updatecasedesc, updatecasestatus)
            return redirect("/caseinfo")

        editcaseid = request.args.get("editcaseid")
        editcasedesc = request.args.get("editcasedesc")
        editcasestatus = request.args.get("editcasestatus")

        return render_template("updateCase.html", editcaseid=editcaseid, editcasedesc=editcasedesc,
                               editcasestatus=editcasestatus)
