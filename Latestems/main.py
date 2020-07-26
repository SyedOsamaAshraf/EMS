
dic={
    "Dashboard":{"Details":"NUll",
                "Performance":"Null",
                 "Trainings":"Null",
                 "Certifications":"Null"
                },
    "Personal Identity Information":{"Name":"Syed Ashrfa",
                                    "Gender":"Male",
                                     "Date of Birth":"18/03/1996",
                                     "Place of Birth":"Lucknow",
                                     "State":"Uttar Pradesh",
                                     "Nationality":"Indian",
                                     "Marital Status":"Single",
                                     "Disability":"None",
                                    },
    "Address":{"Address Type":[{"Present":{"Full Name":"Present",
                                         "Address Line 1":"Nullllllllll",
                                         "Address Line 2":"Nullllllllll",
                                         "Address Line 3":"Nullllllllll",
                                          "City":"Lucknow",
                                          "State":"Uttar Pradesh",
                                          "Pincode":226021,
                                          "Area":"Whatever",
                                          "Langitude":45.02,
                                          "Latitude":45.00,}
                              },
                               {"Permanent":{"Full Name":"Permanent",
                                         "Address Line 1":"xxxxxxxxxxxxxxxxxxxx",
                                         "Address Line 2":"Nullllllllll",
                                         "Address Line 3":"Nullllllllll",
                                          "City":"Lucknow",
                                          "State":"Uttar Pradesh",
                                          "Pincode":226021,
                                          "Area":"Whatever",
                                          "Langitude":45.02,
                                          "Latitude":45.00,}
                               },
                               {"Emergency":{"Full Name":"Emergency",
                                         "Address Line 1":"Nullllllllll",
                                         "Address Line 2":"Nullllllllll",
                                         "Address Line 3":"Nullllllllll",
                                          "City":"Lucknow",
                                          "State":"Uttar Pradesh",
                                          "Pincode":226021,
                                          "Area":"Whatever",
                                          "Langitude":45.02,
                                          "Latitude":45.00,}
                                }]
              },
    "Passport":{"Pasport Number":123456789455,
               "Date of Expiry":"11/11/11"},
    "Aadhaar":{"Number":123456789},

    "Pan":{"Number":123456789},
    
    "Master Data":{"First Name":"XYZ",
                   "Middle Name":"Ool",
                   "Designation":"Principal",
                   "Confirmed":"Y/N",
                   "Role":"Don't know",
                   "Team":"xxxx",
                   "Department":"kll",
                   "Reporting Manager":"sssssss",
                   "Base Location":"Lucknow",
                   "Current Location":"Lucknow",
                   "Delivery Unit":"ddddddd",
                   "Delivery Manager":"ssssssss",
                  },
    "Project":{"Project Code":[0,1,2],
               "From Date":["11/12","12/45","45"],
              "To Date":["11/12","12/45","45"]},
    
}


from flask import Flask,render_template,request
app = Flask(__name__,template_folder='templates', static_folder='static')
import json
import pandas as pd

@app.route('/')
def home():
    return render_template("official.html",data=(dic))

if __name__ == "__main__":
    app.run(debug=True)