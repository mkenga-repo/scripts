import json

import requests
from urllib.parse import urlencode
import urllib
import mysql.connector
from mysql.connector import Error
import datetime



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

#Fetch Matters

class Token:
    def __init__(self,token_url,token_data,token_headers):
        self.token_data = token_data
        self.token_headers = token_headers
        self.token_url = token_url
    def get_auth_token(self):
        auth_request = requests.request("POST",url=self.token_url,data=self.token_data,headers=self.token_headers)
        auth_response = auth_request.json()
        token = auth_response['access_token']
        return token

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
    'username' : f'wmarita@mkenga.dev.com',
    'password' : f'Mc=\EGZ$S#764$',
})

auth_request_params = Token(token_url=auth_url,token_headers=auth_headers,token_data=auth_body)
# auth_token = auth_request_params.get_auth_token()

##Client_ID

class Client_ID:
    def __init__(self, client_id_header, client_id_url):
        self.client_id_header = client_id_header
        self.client_id_url = client_id_url

    def get_client_id(self):
        client_id_request = requests.request("GET",url=self.client_id_url,headers=self.client_id_header)
        client_id_response = client_id_request.json()
        client_id_key = client_id_response ['data']['user']['customer_id']
        return client_id_key
    def get_libraries(self):
        library_request = requests.request("GET", url=self.client_id_url, headers=self.client_id_header)
        library_response = library_request.json()
        library_list = library_response['data']['work']['libraries']
        print(library_list[0]['alias'])
        return library_list[0]['alias']
        # return 'legal_cabinet_legal_drive'



client_id_endpoint = '/api'
client_id_url = base_url + client_id_endpoint
client_id_token = auth_request_params.get_auth_token()
client_id_header = ({
     'X-Auth-Token' : auth_request_params.get_auth_token()
 })

client_id_request_params = Client_ID(client_id_url = client_id_url, client_id_header=client_id_header)
customer_id = client_id_request_params.get_client_id()
library = client_id_request_params.get_libraries()

#Fetch Matters

class Clients:
    def __init__(self,custom1_url,custom1_headers,custom1_params):
        self.custom1_url = custom1_url
        self.custom1_headers = custom1_headers
        self.custom1_params = custom1_params

    def get_clients(self):
        custom1_request = requests.request('GET',url=self.custom1_url,headers=self.custom1_headers,params=self.custom1_params)
        custom1_response = custom1_request.json()
        custom1_list = custom1_response['data']

        for clients in custom1_list:
            if 'id' not in clients:
                return ''
            else:
                client_key = clients['id']
            if 'description' not in clients:
                return ''
            else:
                client_description = clients['description']


            custom1_sql = 'INSERT IGNORE INTO clients(client_key,client_description) VALUES (%s,%s)'
            custom1_values = (client_key,client_description)

            cursor.execute(custom1_sql,custom1_values)
            connection.commit()
            print(cursor.rowcount, " client record inserted.")

client_request_endpoint = f'/api/v2/customers/{customer_id}/libraries/{library}/customs/custom1'
client_request_url = base_url + client_request_endpoint

custom1_request_header = ({
     'X-Auth-Token' : auth_request_params.get_auth_token()
})

custom1_request_params = urllib.parse.urlencode({
    'limit':'9999'
})
client_request = Clients(custom1_url=client_request_url,custom1_headers=custom1_request_header,custom1_params=custom1_request_params)
client_request.get_clients()



class Matters:
    def __init__(self,custom2_url,custom2_headers,custom2_params):
        self.custom2_url = custom2_url
        self.custom2_headers = custom2_headers
        self.custom2_params = custom2_params

    def get_matters(self):
        matter_request = requests.request("GET",url=self.custom2_url,
                                          headers=self.custom2_headers,
                                          params=self.custom2_params
                                          )
        matter_response = matter_request.json()
        # connection = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     database='scriptor',
        #     password='Sm30174026'
        # )
        mycursor = connection.cursor()

        custom2_list = matter_response['data']
        for x in custom2_list:
            ssid = x['ssid']
            matter_key = x['id']
            matter_description = x['description']
            client_key = x['parent']['id']
            unique_key = f'{client_key}.{matter_key}'
            print(ssid,matter_key,matter_description,client_key)

            sql_script = 'INSERT IGNORE INTO matters (ssid, matter_key, matter_description, client_key,unique_key) VALUES (%s, %s, %s, %s, %s)'
            values = (ssid, matter_key, matter_description, client_key, unique_key)
            cursor.execute(sql_script, values)
            connection.commit()
            print(cursor.rowcount, "Matter inserted.")
#
custom2_endpoint = f'/api/v2/customers/{customer_id}/libraries/{library}/customs/custom2'
custom2_request_url = base_url + custom2_endpoint
print(custom2_request_url)

custom2_request_header = ({
     'X-Auth-Token' : auth_request_params.get_auth_token()
})

custom2_request_params = urllib.parse.urlencode({
    'limit':'9999'
})
#
custom2_request = Matters(custom2_url=custom2_request_url,custom2_headers=custom2_request_header,custom2_params=custom2_request_params)
custom2_request.get_matters()
#

#Library Workspaces.


class Workspaces:
    def __init__(self,workspace_url,workspace_header):
        self.workspace_url = workspace_url
        self.workspace_header = workspace_header
        # self.workspace_params = workspace_params

    def get_workspaces(self):
            workspace_request = requests.request("GET",url=self.workspace_url,headers=self.workspace_header)
            workspace_response = workspace_request.json()
            workspace_data = workspace_response['data']['results']
            print(len(workspace_data))
            # return True

            # return print(workspace_data)

            for workspace in workspace_data:

                if 'create_date' not in workspace:
                    create_date = ''
                else:
                    create_date = workspace['create_date']
                if 'database' not in workspace:
                    database = ''
                else:
                    database = workspace['database']
                if 'default_security' not in workspace:
                    security = ''
                else:
                    security = workspace['default_security']
                if 'name' not in workspace:
                    workspace_name = ''
                else:
                    workspace_name = workspace['name']
                if 'id' not in workspace:
                    workspace_id = ''
                else:
                    workspace_id = workspace['id']
                if 'owner' not in workspace:
                    owner = ''
                else:
                    owner = workspace['owner']

                if 'custom1' not in workspace:
                    client_key = ''
                else:
                    client_key = workspace['custom1']
                if 'custom2' not in workspace:
                    matter_key = ''
                else:
                    matter_key = workspace['custom2']
                if 'custom29' not in workspace:
                    practice_area = ''
                else:
                    practice_area = workspace['custom29']
                if 'document_number' not in workspace:
                    no_of_documents = ''
                else:
                    no_of_documents = int(workspace['document_number'])
                if 'custom2_description' not in workspace:
                    matter_description = ''
                else:
                    matter_description = workspace['custom2_description']




                # print(create_date,database,security)

                workspace_sql_script = 'INSERT IGNORE INTO Workspaces (workspace_id,workspace_name,library,owner,security,created_date,client_key,matter_key,matter_description,practice_area_key,total_documents) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                workspace_values = (workspace_id,workspace_name,database,owner,security,create_date,client_key,matter_key,matter_description,practice_area,no_of_documents)
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    database='scriptor',
                    password='Sm30174026'
                )
                mycursor = connection.cursor()

                mycursor.execute(workspace_sql_script,workspace_values)
                connection.commit()


                print(mycursor.rowcount, " workspace record inserted.")
            return True








workspace_endpoint_url = f'/api/v2/customers/{customer_id}/libraries/{library}/workspaces?total=true&limit=9999'
workspace_request_url = base_url + workspace_endpoint_url
workspaces_request_headers = ({
    'X-Auth-Token': auth_request_params.get_auth_token()
})

# workspaces_request_params = urllib.parse.urlencode({
#     'limit': '9999'
# })

workspace_request = Workspaces(workspace_url=workspace_request_url,workspace_header=workspaces_request_headers)
workspace_request.get_workspaces()

