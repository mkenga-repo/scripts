import requests
from urllib.parse import urlencode
import urllib
import mysql.connector
from mysql.connector import Error
import datetime
import csv
#get batch of 100 from db

#start foreach loop
body = {
    #add variables for each request param
  "name": "Demo Workspace - Wycliff",
  "description": "Workspace Created For Demo Purposes",
  "default_security": "public",
  "custom1": "10"
}

header = {
    'X-Auth-Token' : 'wBhspzSLZF6hJmBtnVtq6YPuCIaZRwBO0oMB7ddTN98'
}
url = 'https://cloudimanage.com/api/v2/customers/1686/libraries/Dev/workspaces'

# c_request = requests.request("POST",url=url,headers=header,json=body)
# response = c_request.json()
# print(response)

connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    database='scriptor',
                    password='Sm30174026'
                )
mycursor = connection.cursor()

data = 'SELECT * FROM custom1 LIMIT 3000'

mycursor.execute(data)
x = mycursor.fetchall()
response_list = []


for line in x:
    name = line[2]
    description = line[2]
    custom1 = line[1]
    body = {
        "name": name,
        "description": description,
        "default_security": "public",
        "custom1": custom1
    }
    header = {
        'X-Auth-Token': 'DaJQuzbt06mLietq4tunqzxKNGEzp6dOBrSnq1QPUgw'
    }
    url = 'https://cloudimanage.com/api/v2/customers/1764/libraries/Archived_Matters/workspaces'

    c_request = requests.request("POST",url=url,headers=header,json=body)
    response = c_request.json()
    response_data = response['data']
    print(response_data)
    # # response_list.append(body)


    # custom1_sql = f'INSERT IGNORE INTO response(json_response) VALUES ({response_data})'
    # # custom1_values = response_data
    #
    # connection = mysql.connector.connect(
    #     host='localhost',
    #     user='root',
    #     database='scriptor',
    #     password='Sm30174026'
    # )
    #
    # mycursor = connection.cursor()
    #
    # mycursor.execute(custom1_sql)
    # connection.commit()
    # print(mycursor.rowcount, " client record inserted.")


