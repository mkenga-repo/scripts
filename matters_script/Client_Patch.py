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

data = 'SELECT * FROM client_patch LIMIT 3000'

mycursor.execute(data)
x = mycursor.fetchall()
response_list = []


for line in x:
    alias = line[1]
    description = line[2]
    print(f'Client Id: {alias}.\n Client Description: {description}.')
    url = f'https://cloudimanage.com/api/v2/customers/1764/libraries/Current_Matters/customs/custom1/{alias}'

    body = {
        "hipaa": False,
        "enabled": True,
        "description": f"{description}"
    }
    header = {
        'X-Auth-Token': 'Lljvugm6rfowtkoY-0GxFpQYLgvEu5kLWWyKwcA0oBs'
    }
    c_request = requests.request("PATCH",url=url,headers=header,json=body)
    response = c_request.content
    # response_data = response['data']
    print(response)