
import requests
from urllib.parse import urlencode
import urllib
import mysql.connector
from mysql.connector import Error
import datetime
import csv



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

class Token:
    def __init__(self,token_url,token_data,token_headers):
        self.token_data = token_data
        self.token_headers = token_headers
        self.token_url = token_url
    def get_auth_token(self):
        auth_request = requests.request("POST",url=self.token_url,data=self.token_data,headers=self.token_headers)
        auth_response = auth_request.json()
        token = auth_response['access_token']
        # return token
        print(token)

base_url = 'https://cloudimanage.com'
auth_endpoint = '/auth/oauth2/token'
auth_url = base_url + auth_endpoint
auth_headers = {
    "Accept": "application/json",
    # "Accept-Encoding": "utf-8",
    "Content-Type": "application/x-www-form-urlencoded",
}
# email = input('Email: ')
# password = input('Password: ')
auth_body = urllib.parse.urlencode({
    'grant_type': 'password',
    'client_id': '098d18f0-586f-413b-8bd2-fc8f2ff5cb46',
    'client_secret': '1dec4003-0a4b-4703-906d-85ac9f332c31',
    'username' : f'CloudAdmin@salcaldeira.com',
    'password' : f'XNY5q6Rm2q3vavpW',
})

auth_request_params = Token(token_url=auth_url,token_headers=auth_headers,token_data=auth_body)
auth_token = auth_request_params.get_auth_token()


with open('/Users/sabir/Downloads/Archived_Library Clients-utf copy.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.DictReader(file)




    # displaying the contents of the CSV file
    for lines in csvFile:
        # print(lines['\ufeffclient_id'])
        client_id = lines['\ufeffclient_id']
        client_description = lines['client_description']

        header = ({
            'X-Auth-Token': auth_request_params.get_auth_token()
        })
        payload = urllib.parse.urlencode({
            "description": client_description,
            "enabled": 'true',
            "hipaa": 'false',
            "id": client_id

        })
        client_url = 'https://cloudimanage.com/work/api/v2/customers/1764/libraries/Archived_Matters/customs/custom1'

        client_post = requests.request('POST',url=client_url,headers=header,data=payload)
        response = client_post.json()
        print(response)

        # custom1_sql = 'INSERT IGNORE INTO custom1(client_id,client_description) VALUES (%s,%s)'
        # custom1_values = (client_id, client_description)
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
        # mycursor.execute(custom1_sql, custom1_values)
        # connection.commit()
        # print(mycursor.rowcount, " client record inserted.")
