from flask import Flask, render_template, request, redirect, url_for

class Address:
    def __init__(self, read_instance, delete_instance, update_instance):
        self.read_instance = read_instance
        self.delete_instance = delete_instance
        self.update_instance = update_instance

    def addressinfo(self, request):
        if request.method == "POST":
            if "action" in request.form:
                if request.form["action"] == "delete":
                    addressid = request.form["deleteaddressid"]
                    self.delete_instance.delete_addressinfo(addressid)
                elif request.form["action"] == "edit":
                    editaddressid = request.form["editaddressid"]
                    edithouseholdno = request.form["edithouseholdno"]
                    editzone = request.form["editzone"]
                    editstreetname = request.form["editstreetname"]
                    editcity = request.form["editcity"]
                    editprovince = request.form["editprovince"]

                    return redirect(url_for("updateAddressInfo_route", editaddressid=editaddressid,
                                            edithouseholdno=edithouseholdno, editzone=editzone,
                                            editstreetname=editstreetname, editcity=editcity,
                                            editprovince=editprovince))

        addressinfo = self.read_instance.read_addressinfo()
        return render_template("addressinfo.html", addressinfo=addressinfo)

    def updateAddressInfo(self, request):
        if request.method == "POST":
            updateaddressid = request.form["updateaddressid"]
            updatehouseholdno = request.form["updatehouseholdno"]
            updatezone = request.form["updatezone"]
            updatestreetname = request.form["updatestreetname"]
            updatecity = request.form["updatecity"]
            updateprovince = request.form["updateprovince"]

            self.update_instance.update_addressinfo(updateaddressid, updatehouseholdno, updatezone, updatestreetname,
                                                     updatecity, updateprovince)
            return redirect("/addressinfo")

        editaddressid = request.args.get("editaddressid")
        edithouseholdno = request.args.get("edithouseholdno")
        editzone = request.args.get("editzone")
        editstreetname = request.args.get("editstreetname")
        editcity = request.args.get("editcity")
        editprovince = request.args.get("editprovince")

        return render_template("updateAddress.html", editaddressid=editaddressid,
                               edithouseholdno=edithouseholdno, editzone=editzone,
                               editstreetname=editstreetname, editcity=editcity,
                               editprovince=editprovince)
