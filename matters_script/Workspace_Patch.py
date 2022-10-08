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

data = 'SELECT * FROM workspace_patch LIMIT 3000'

mycursor.execute(data)
x = mycursor.fetchall()
response_list = []

for line in x:
    # print(line)
    workspace_id = line[1]
    workspace_name = line[2]
    client_key = line[3]

    # print(workspace_id,workspace_name,client_key)
    # print(f'Client Id: {alias}.\n Client Description: {description}.')
    workspace_update_url = f'https://cloudimanage.com/api/v2/customers/1764/libraries/Archived_Matters/workspaces/{workspace_id}'
    client_update_url = f'https://cloudimanage.com/api/v2/customers/1764/libraries/Archived_Matters/customs/custom1/{client_key}'
    # url = f'https://cloudimanage.com/api/v2/customers/1764/libraries/Current_Matters/customs/custom2/{alias}'
    #
    body = {
        "name": workspace_name
    }
    header = {
        'X-Auth-Token': 'N9h3yE5VOmmws760bdTJwIKd6um6WJcxaF2srvxUWSw'
    }

    client_update_body = {
        "description": workspace_name
    }

    # param = {
    #     "parent_alias" : line[1]
    # }
    # c_request = requests.request("PATCH",url=url,headers=header,json=body,params=param)
    ws_request = requests.request("PATCH", url=workspace_update_url, headers=header, json=body)
    response = ws_request.content
    # # response_data = response['data']
    print(response)
    c_request = requests.request("PATCH",url=client_update_url,json=client_update_body,headers=header)
    c_response = c_request.content
    print(f"C_Response: {c_response}")