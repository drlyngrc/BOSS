from flask import Flask, render_template, request, redirect, url_for

class Resident:
    def __init__(self, read_instance, delete_instance, update_instance):
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def residentinfo(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "delete":
                    barangayid = request.form["deletebarangayid"]
                    self.delete_instance.delete_residentinfo(barangayid)
                elif request.form["action"] == "edit":
                    editbarangayid = request.form["editbarangayid"]
                    editcategory = request.form["editcategory"]
                    editlastname = request.form["editlastname"]
                    editfirstname = request.form["editfirstname"]
                    editmiddlename = request.form["editmiddlename"]
                    editsex = request.form["editsex"]
                    editbirthdate = request.form["editbirthdate"]
                    editbirthplace = request.form["editbirthplace"]
                    editreligion = request.form["editreligion"]
                    editcivilstat = request.form["editcivilstat"]
                    editcitizenship = request.form["editcitizenship"]
                    editvoterprecinct = request.form["editvoterprecinct"]
                    editcontactno = request.form["editcontactno"]

                    return redirect(url_for("updateResidentInfo_route", editbarangayid=editbarangayid, editcategory=editcategory,
                                            editlastname=editlastname, editfirstname=editfirstname, editmiddlename=editmiddlename,
                                            editsex=editsex, editbirthdate=editbirthdate, editbirthplace=editbirthplace,
                                            editreligion=editreligion, editcivilstat=editcivilstat,
                                            editcitizenship=editcitizenship, editvoterprecinct=editvoterprecinct,
                                            editcontactno=editcontactno))

        residentinfo = self.read_instance.read_residentinfo()
        return render_template("residentinfo.html", residentinfo=residentinfo)

    def updateResidentInfo(self, request):
        if request.method == "POST":
            updatebarangayid = request.form["updatebarangayid"]
            updatecategory = request.form["updatecategory"]
            updatelastname = request.form["updatelastname"]
            updatefirstname = request.form["updatefirstname"]
            updatemiddlename = request.form["updatemiddlename"]
            updatesex = request.form["updatesex"]
            updatebirthdate = request.form["updatebirthdate"]
            updatebirthplace = request.form["updatebirthplace"]
            updatereligion = request.form["updatereligion"]
            updatecivilstat = request.form["updatecivilstat"]
            updatecitizenship = request.form["updatecitizenship"]
            updatevoterprecinct = request.form["updatevoterprecinct"]
            updatecontactno = request.form["updatecontactno"]

            self.update_instance.update_residentinfo(updatebarangayid, updatecategory, updatelastname, updatefirstname,
                                                     updatemiddlename, updatesex, updatebirthdate, updatebirthplace,
                                                     updatereligion, updatecivilstat, updatecitizenship,
                                                     updatevoterprecinct, updatecontactno)
            return redirect("/residentinfo")

        editbarangayid = request.args.get("editbarangayid")
        editcategory = request.args.get("editcategory")
        editlastname = request.args.get("editlastname")
        editfirstname = request.args.get("editfirstname")
        editmiddlename = request.args.get("editmiddlename")
        editsex = request.args.get("editsex")
        editbirthdate = request.args.get("editbirthdate")
        editbirthplace = request.args.get("editbirthplace")
        editreligion = request.args.get("editreligion")
        editcivilstat = request.args.get("editcivilstat")
        editcitizenship = request.args.get("editcitizenship")
        editvoterprecinct = request.args.get("editvoterprecinct")
        editcontactno = request.args.get("editcontactno")

        return render_template("updateResident.html", editbarangayid=editbarangayid, editcategory=editcategory,
                               editlastname=editlastname, editfirstname=editfirstname, editmiddlename=editmiddlename,
                               editsex=editsex, editbirthdate=editbirthdate, editbirthplace=editbirthplace,
                               editreligion=editreligion, editcivilstat=editcivilstat,
                               editcitizenship=editcitizenship, editvoterprecinct=editvoterprecinct,
                               editcontactno=editcontactno)
