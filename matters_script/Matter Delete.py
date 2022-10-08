import requests
from urllib.parse import urlencode
import urllib
import mysql.connector
from mysql.connector import Error
import datetime
import csv

connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    database='scriptor',
                    password='Sm30174026'
                )
mycursor = connection.cursor()
data = 'SELECT * FROM matters LIMIT 3000'

mycursor.execute(data)
x = mycursor.fetchall()
response_list = []

for line in x:
    matter_key = line[2]
    client_key = line[4]
    # print(line)

    matter_url = f'https://cloudimanage.com/api/v2/customers/1686/libraries/Dev/customs/custom2/{matter_key}'


    matter_header = {
        'X-Auth-Token' : 'LL4z3FE74LNa32V2yAdTWqjug5uGLrR7V9G03bofAH0'
    }

    matter_params = {
        'parent_alias' : client_key
    }

    matter_delete_request = requests.request("DELETE",url=matter_url,headers=matter_header,params=matter_params)
    matter_delete_response = matter_delete_request.content
    print(matter_delete_response)