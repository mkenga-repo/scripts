import requests
from urllib.parse import urlencode
import urllib
import mysql.connector
from mysql.connector import Error
import json

connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    database='scriptor',
                    password='Sm30174026'
                )
mycursor = connection.cursor()

data = 'SELECT * FROM matter_patch LIMIT 3000'

mycursor.execute(data)
x = mycursor.fetchall()
response_list = []


for line in x:
    print(line)
    alias = line[2]
    description = line[3]
    print(f'Client Id: {alias}.\n Client Description: {description}.')
    url = f'https://cloudimanage.com/api/v2/customers/1764/libraries/Current_Matters/customs/custom2/{alias}'

    body = {
        "hipaa": False,
        "enabled": True,
        "description": f"{description}"
    }
    header = {
        'X-Auth-Token': 'iU5tkJ1J_j7B8NvSRB4bMQHpfXSYBalHMSOTXRIgwbk'
    }

    param = {
        "parent_alias" : line[1]
    }
    c_request = requests.request("PATCH",url=url,headers=header,json=body,params=param)
    response = c_request.content
    # response_data = response['data']
    print(response)