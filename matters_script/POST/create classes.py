import os

import mysql.connector

db_connection = mysql.connector.connect(
    host= 'localhost',
    database= 'scriptor',
    user= 'root',
    password= 'Sm30174026'
)

cursor = db_connection.cursor()
sql_query = 'SELECT * FROM clients'

cursor.execute(sql_query)
list= cursor.fetchall()

for client in list:
    id = client[0]
    client_key = client[1]
    c_description = client[2]
    payload = {'id' : id,'client_key' : client_key,'c_descriprion' : c_description}



