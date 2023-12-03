from flask import Flask, render_template, request, redirect, url_for

class Medical:
    def __init__(self, read_instance, delete_instance, update_instance):
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def medicalinfo(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "delete":
                    medicalid = request.form["deletemedicalid"]
                    self.delete_instance.delete_medicalinfo(medicalid)
                elif request.form["action"] == "edit":
                    editmedicalid = request.form["editmedicalid"]
                    editbmiclassification = request.form["editbmiclassification"]
                    editmedicalcondition = request.form["editmedicalcondition"]
                    editcovidvaccinated = request.form["editcovidvaccinated"]
                    editmaintenancemedicine = request.form["editmaintenancemedicine"]
                    editphysicalfitness = request.form["editphysicalfitness"]

                    return redirect(url_for("updateMedicalInfo_route", editmedicalid=editmedicalid,
                                            editbmiclassification=editbmiclassification,
                                            editmedicalcondition=editmedicalcondition,
                                            editcovidvaccinated=editcovidvaccinated,
                                            editmaintenancemedicine=editmaintenancemedicine,
                                            editphysicalfitness=editphysicalfitness))

        medicalinfo = self.read_instance.read_medicalinfo()
        return render_template("medicalinfo.html", medicalinfo=medicalinfo)

    def updateMedicalInfo(self, request):
        if request.method == "POST":
            updatemedicalid = request.form["updatemedicalid"]
            updatebmiclassification = request.form["updatebmiclassification"]
            updatemedicalcondition = request.form["updatemedicalcondition"]
            updatecovidvaccinated = request.form["updatecovidvaccinated"]
            updatemaintenancemedicine = request.form["updatemaintenancemedicine"]
            updatephysicalfitness = request.form["updatephysicalfitness"]

            self.update_instance.update_medicalinfo(updatemedicalid, updatebmiclassification, updatemedicalcondition,
                                                     updatecovidvaccinated, updatemaintenancemedicine,
                                                     updatephysicalfitness)
            return redirect("/medicalinfo")

        editmedicalid = request.args.get("editmedicalid")
        editbmiclassification = request.args.get("editbmiclassification")
        editmedicalcondition = request.args.get("editmedicalcondition")
        editcovidvaccinated = request.args.get("editcovidvaccinated")
        editmaintenancemedicine = request.args.get("editmaintenancemedicine")
        editphysicalfitness = request.args.get("editphysicalfitness")

        return render_template("updateMedical.html", editmedicalid=editmedicalid,
                               editbmiclassification=editbmiclassification,
                               editmedicalcondition=editmedicalcondition,
                               editcovidvaccinated=editcovidvaccinated,
                               editmaintenancemedicine=editmaintenancemedicine,
                               editphysicalfitness=editphysicalfitness)
