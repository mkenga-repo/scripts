import json

import requests
from urllib.parse import urlencode
import urllib
import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='scriptor',
                                         user='root',
                                         password='Sm30174026',
                                         port='3306')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
# # finally:
# #     if connection.is_connected():
# #         cursor.close()
# #         connection.close()
# #         print("MySQL connection is closed")
# # url = 'https://catfact.ninja/fact'
# # response = requests.request('GET',url)
# # print(response.json())
#
base_url = 'https://cloudimanage.com'
auth_end_point = '/auth/oauth2/token'
url = base_url + auth_end_point #Oauth URL
disc_url = base_url + '/api' #Discovery URL

headers = {
    "Accept": "application/json",
    # "Accept-Encoding": "utf-8",
    "Content-Type": "application/x-www-form-urlencoded",
}
params = urllib.parse.urlencode({
    'grant_type': 'password',
    'client_id': '098d18f0-586f-413b-8bd2-fc8f2ff5cb46',
    'client_secret': '1dec4003-0a4b-4703-906d-85ac9f332c31',
    'username' : 'CloudAdmin@olajideoyewole.com',
    'password' : '/Cg3Y+kZ(W298@',
})

response = requests.request("POST",url,data=params,headers=headers)

json_response = response.json()

token = json_response['access_token']
# print(token)

##Customer ID

disc_header = ({
    'X-Auth-Token' : token
})

disc_request = requests.request('GET',disc_url,headers=disc_header)
disc_response = disc_request.json()
customer_id = disc_response['data']['user']['customer_id']
library_response = disc_response['data']['work']['libraries'] ###Get Library
library = library_response[0]['alias']

# print(library)
# {{urlPrefix}}/api/v2/customers/{{customerId}}/libraries/{{libraryName}}/customs/custom1

#Get Custom 1

custom1_url = base_url + f'/api/v2/customers/{customer_id}/libraries/{library}/customs/custom1'

custom1_header = ({
    'X-Auth-Token' : token
})

custom1_params = urllib.parse.urlencode({
    'limit':'9999'
})


custom1_request = requests.request('GET',custom1_url,headers=custom1_header, params=custom1_params)
custom1_response = custom1_request.json()

custom1_list = custom1_response['data']
#Loop through Clients
#

connection = mysql.connector.connect(host='localhost',
                                         database='scriptor',
                                         user='root',
                                         password='Sm30174026')

mycursor = connection.cursor()

for x in custom1_list:
    client_key = x['id']
    description = x['description']
    # print (f'Client: {client_key} - Description: {description}')
    sql = "INSERT IGNORE INTO clients (client_key,client_description) VALUES (%s,%s)"
    values =[client_key,description]
    mycursor.execute(sql,values)
    connection.commit()
    print(mycursor.rowcount, "record inserted.")

#
#
#
