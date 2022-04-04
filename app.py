from calendar import month
from flask import Flask, request
import requests, json
from flask import render_template
from datetime import date, datetime, timedelta


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/api")
def api():
    today = date.today()
    new_date = today - timedelta(weeks = 2)
    url = "https://e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"
    d3 = new_date.strftime("%y-%m-%d")
    payload = None
    if request.args.get('date') != None:
        print("AICI")
        d3 = request.args.get('date')
        payload = "{\n\"pageIndex\": 0,\n\"pageSize\": 2000,\n\"sortProperties\": [],\n\"startPublicationDate\": \""+d3+"\",\n\"startEstimatedValueRon\":200000,\n\"cPVText\": \"48\",\n\"sysNoticeTypeIds\": [2],\n\"sysProcedureStateId\": 2\n}"
        payload2 = "{\n\"pageIndex\": 0,\n\"pageSize\": 2000,\n\"sortProperties\": [],\n\"startPublicationDate\": \""+d3+"\",\n\"startEstimatedValueRon\":200000,\n\"cPVText\": \"32\",\n\"sysNoticeTypeIds\": [2],\n\"sysProcedureStateId\": 2\n}"
        payload3 = "{\n\"pageIndex\": 0,\n\"pageSize\": 2000,\n\"sortProperties\": [],\n\"startPublicationDate\": \""+d3+"\",\n\"startEstimatedValueRon\":200000,\n\"cPVText\": \"302\",\n\"sysNoticeTypeIds\": [2],\n\"sysProcedureStateId\": 2\n}"
    
    else:
        payload = "{\n\"pageIndex\": 0,\n\"pageSize\": 2000,\n\"sortProperties\": [],\n\"startPublicationDate\": \"20"+d3+"\",\n\"startEstimatedValueRon\":200000,\n\"cPVText\": \"48\",\n\"sysNoticeTypeIds\": [2],\n\"sysProcedureStateId\": 2\n}"
        payload2 = "{\n\"pageIndex\": 0,\n\"pageSize\": 2000,\n\"sortProperties\": [],\n\"startPublicationDate\": \"20"+d3+"\",\n\"startEstimatedValueRon\":200000,\n\"cPVText\": \"32\",\n\"sysNoticeTypeIds\": [2],\n\"sysProcedureStateId\": 2\n}"
        payload3 = "{\n\"pageIndex\": 0,\n\"pageSize\": 2000,\n\"sortProperties\": [],\n\"startPublicationDate\": \"20"+d3+"\",\n\"startEstimatedValueRon\":200000,\n\"cPVText\": \"302\",\n\"sysNoticeTypeIds\": [2],\n\"sysProcedureStateId\": 2\n}"
        print(d3)
    print(payload)
    headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://e-licitatie.ro/pub/notices/contract-notices/list/0/0',
    'Cookie': '_HttpSessionID=914B3407CD254F97990834C2BE327756'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response2 = requests.request("POST", url, headers=headers, data=payload2)
    response3 = requests.request("POST", url, headers=headers, data=payload3)
    data = response.json()
    data2 = response2.json()
    data3 = response3.json()
    filtered = list()
    for datum in data["items"]:
        if "48" in  datum["cpvCodeAndName"][:2] or "32" in  datum["cpvCodeAndName"][:2]:
            if datum not in filtered:
                filtered.append(datum)
        else:    
            url = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetSection21View/?initNoticeId="+str(datum["cNoticeId"])+"&sysNoticeTypeId=2"

            payload = ""
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'https://e-licitatie.ro/pub/notices/contract-notices/list/0/0',
                'Cookie': '_HttpSessionID=F3B058C4644345729DC7B372A21639F5'
                }

            response = requests.request("GET", url, headers=headers, data=payload)

            try:
                    lista = response.json()["section22"]["supplementaryCpvCode"]
                    if lista != None:
                        for elem in lista:
                            if "48" in  elem[:2]  or "32" in  elem[:2]:
                                if datum not in filtered:
                                    filtered.append(datum)

            except Exception as e:
                    print(e)

    for datum in data2["items"]:
        if "48" in  datum["cpvCodeAndName"][:2] or "32" in  datum["cpvCodeAndName"][:2]:
            if datum not in filtered:
                filtered.append(datum)
        else:    
            url = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetSection21View/?initNoticeId="+str(datum["cNoticeId"])+"&sysNoticeTypeId=2"

            payload = ""
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'https://e-licitatie.ro/pub/notices/contract-notices/list/0/0',
                'Cookie': '_HttpSessionID=F3B058C4644345729DC7B372A21639F5'
                }

            response = requests.request("GET", url, headers=headers, data=payload)

            try:
                    lista = response.json()["section22"]["supplementaryCpvCode"]
                    if lista != None:
                        for elem in lista:
                            if "48" in  elem[:2]  or "32" in  elem[:2]:
                                if datum not in filtered:
                                    filtered.append(datum)

            except Exception as e:
                    print(e)

    for datum in data3["items"]:
        if "30" in  datum["cpvCodeAndName"][:2]:
            if datum not in filtered:
                filtered.append(datum)
        else:    
            url = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetSection21View/?initNoticeId="+str(datum["cNoticeId"])+"&sysNoticeTypeId=2"

            payload = ""
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'https://e-licitatie.ro/pub/notices/contract-notices/list/0/0',
                'Cookie': '_HttpSessionID=F3B058C4644345729DC7B372A21639F5'
                }

            response = requests.request("GET", url, headers=headers, data=payload)

            try:
                    lista = response.json()["section22"]["supplementaryCpvCode"]
                    if lista != None:
                        for elem in lista:
                            if "30" in  elem[:2]:
                                if datum not in filtered:
                                    filtered.append(datum)

            except Exception as e:
                    print(e)

    newlist = sorted(filtered, key=lambda d: d['estimatedValueRon'], reverse=True) 
    return {"data": newlist}

if __name__ == "__main__":
    app.run(debug=True, port=5001)