from flask import Flask, render_template, request, redirect, url_for

class Student:
    def __init__(self, read_instance, delete_instance, update_instance):
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def studentinfo(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "delete":
                    studentid = request.form["deletestudentid"]
                    self.delete_instance.delete_studentinfo(studentid)
                elif request.form["action"] == "edit":
                    editstudentid = request.form["editstudentid"]
                    edityearlevel = request.form["edityearlevel"]
                    editschool = request.form["editschool"]
                    editacademicyear = request.form["editacademicyear"]
                    editscholarship = request.form["editscholarship"]

                    return redirect(url_for("updateStudentInfo_route", editstudentid=editstudentid,
                                            edityearlevel=edityearlevel,
                                            editschool=editschool, editacademicyear=editacademicyear,
                                            editscholarship=editscholarship))

        studentinfo = self.read_instance.read_studentinfo()
        return render_template("studentinfo.html", studentinfo=studentinfo)

    def updateStudentInfo(self, request):
        if request.method == "POST":
            updatestudentid = request.form["updatestudentid"]
            updateyearlevel = request.form["updateyearlevel"]
            updateschool = request.form["updateschool"]
            updateacademicyear = request.form["updateacademicyear"]
            updatescholarship = request.form["updatescholarship"]

            self.update_instance.update_studentinfo(updatestudentid, updateyearlevel, updateschool,
                                                     updateacademicyear, updatescholarship)
            return redirect("/studentinfo")

        editstudentid = request.args.get("editstudentid")
        edityearlevel = request.args.get("edityearlevel")
        editschool = request.args.get("editschool")
        editacademicyear = request.args.get("editacademicyear")
        editscholarship = request.args.get("editscholarship")

        return render_template("updateStudent.html", editstudentid=editstudentid, edityearlevel=edityearlevel,
                               editschool=editschool, editacademicyear=editacademicyear, editscholarship=editscholarship)
