import requests
from urllib.parse import urlencode
import urllib
import mysql.connector
from mysql.connector import Error
import datetime
import csv

customer_id = 1686
library = 'Dev'
endpoint = f'https://cloudimanage.com/api/v2/customers/1686/libraries/Dev/folders'
header = ({
    'X-Auth-Token': 'XqcfkUZD-e-4YvBayg1zxjgQNTdC2apHJOFcYOA06I0'
})

folders_request = requests.request("GET",url=endpoint,headers=header)
folders_response = folders_request.json()
folder_list = folders_response['data']


for folder in folder_list:
    folder_id = folder['id']
    if folder ['has_documents'] == False and folder ['has_subfolders'] == False:
        # folder_delete_url = f"https://cloudimanage.com/api/v2/customers/{customer_id}/libraries/{library}/folders/{folder_id}"
        # folder_delete_header = header
        # folder_delete_request = requests.request("DELETE",url=folder_delete_url,headers=folder_delete_header)
        # folder_delete_response = folder_delete_request.content
        pass
    else:
        folder_children_url = f'https://cloudimanage.com/api/v2/customers/{customer_id}/libraries/{library}/folders/{folder_id}/children'
        folder_children_header= header
        folder_children_request = requests.request("GET",url=folder_children_url,headers=folder_children_header)
        folder_children_response = folder_children_request.json()
        folder_children_data = folder_children_response ['data']
        print(folder_children_data)
        for folder_subchildren in folder_children_data:
            print(folder_subchildren)
























