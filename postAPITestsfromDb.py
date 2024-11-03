import requests
import json

import utilities
from payload import *
from utilities.configurations import *
from utilities.resources import *

url= getConfig()['API']['endpoint']+ApiResources.addBook
query = 'select * from Books'
json=buildPayloadFromDB(query)
headers={"Content-Type": "application/json"}
addBook_response = requests.post(url=url, json=json, headers=headers)
print(addBook_response.status_code)
print(addBook_response.json())
bookid = addBook_response.json()['ID']
print(bookid)

url= getConfig()['API']['endpoint']+ApiResources.deleteBook
json= {"ID": bookid}
headers={"Content-Type": "application/json"}
delete_response = requests.post(url=url, headers=headers, json=json)
print(delete_response.status_code)
assert delete_response.status_code == 200
print(delete_response.json()['msg'])
assert delete_response.json()['msg'] == 'book is successfully deleted'