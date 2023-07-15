#!flask/bin/python
#test API to consume data with any frontend or backend
#uses flask to make a localhost api for testing/off cloud dev purposes
#@author stinsley


from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

data = [{
    "id": 3290,
    "unit":u"ER",
    "unitName": u"Emergency Department",
    "certName": u"BLS",
    "certTrack": u"PEOPLESOFT",
  }, {
    "id": 3290,
    "unit":u"ER",
    "unitName": u"Emergency Department",
    "certName": u"ACLS - RN ONLY",
    "certTrack": u"PEOPLESOFT",
  }, {
    "id": 3290,
    "unit":u"ER",
    "unitName": u"Emergency Department",
    "certName": u"PALS - RN ONLY",
    "certTrack": u"PEOPLESOFT",
  }, {
    "id": 3290,
    "unit":u"ER",
    "unitName": u"Emergency Department",
    "certName": u"POCT - ACCUCHECK",
    "certTrack": u"PEOPLESOFT",
  }, {
    "id": 3290,
    "unit":"ER",
    "unitName": u"Emergency Department",
    "certName": u"POCT - URINE PREGNANCY",
    "certTrack": u"PEOPLESOFT",
  }, {
    "id": 3290,
    "unit":u"ER",
    "unitName": u"Emergency Department",
    "certName": u"POCT - RAPID STREP",
    "certTrack": u"PEOPLESOFT",
  }, {
    "id": 3290,
    "unit":u"ER",
    "unitName": u"Emergency Department",
    "certName": u"POCT - CARDIAC MARKERS",
    "certTrack": u"PEOPLESOFT",
  }, {
    "id": 3290,
    "unit":u"ER",
    "unitName": u"Emergency Department",
    "certName": u"POCT - URINE DIP",
    "certTrack": u"PEOPLESOFT",
  },{
    "id": 3290,
    "unit":u"ER",
    "unitName": u"test Department",
    "certName": u"test - URINE DIP",
    "certTrack": u"PEOPLESOFT",
  }]

data2 = [{
  "id":5,
  "unitName":"Emergency woo woo",
  "certName":"test test",
  "certTrack":"tracking woot",
}]

volume =[
  {"volume":[    
    {"date":"2019-11-01", "projected":210,"plan":242 },    
    {"date":"2019-11-02", "projected":213,"plan":242 },    
    {"date":"2019-11-03", "projected":212,"plan":242 },    
    {"date":"2019-11-04", "projected":215,"plan":242 },    
]}]

hppv =[
  
    {"date":"2019-11-04","name":"projected","value":2.72 }, 
    {"name":"plan","value":3.1 }, 
]

table =[
{"Type": "Recomended Hours by Medecipher",
     "Date": "December",
    "time1": 12,
    "time2": 12,
    "time3": 12,
    "time4": 12,
    "time5": 12,
    "time6": 12,
    "time7": 12,
    "time8": 12,
    "time9": 12,
    "time10": 12,
    "time11": 12,
    "time12": 12,
    "total":144},
    {"Type": "Total Hours Scheduled",
    "Date": "November",
    "time1": 10,
    "time2": 14,
    "time3": 18,
    "time4": 18,
    "time5": 20,
    "time6": 18,
    "time7": 20,
    "time8": 18,
    "time9": 12,
    "time10": 12,
    "time11": 10,
    "time12": 10,
    "total":170},
]


mult =[
{"name": "Projected - Conservative Flexing",
      "series": [
        {
          "name": "0",
          "value": 27,
        },
      ]
 },
 {
  "name": "Planned - Staffing Level",
  "series": [
    {
      "name": "0",
      "value": 25,
    },]
 }]

 
@app.route("/api/dept-data", methods=["GET"])
def get_data():
    return jsonify(data)   

@app.route("/api/dept-data2", methods=["GET"])
def get_data2():
    return jsonify(data2)   
@app.route("/api/pat-volume", methods=["GET"])
def get_volume():
    return jsonify(volume)
@app.route("/api/hppv", methods=["GET"])
def get_hppv():
    return jsonify(hppv)



if __name__ == "__main__":
    app.run(debug=True)
