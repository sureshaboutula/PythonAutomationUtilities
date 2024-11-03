import requests
import json

import utilities
from payload import *
from utilities.configurations import *
from utilities.resources import *

addBook_response = requests.post(
    # url='http://216.10.245.166/Library/Addbook.php',
    url= getConfig()['API']['endpoint']+ApiResources.addBook,
    json=addBookPayload("isbntest2"),
    headers={
        "Content-Type": "application/json"
    }
)
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))
bookId = response_json['ID']
print(bookId)
# resp_msg = response_json['Msg']
# print(resp_msg)

# Delete Book

response_delete = requests.post(
    url=getConfig()['API']['endpoint']+ApiResources.deleteBook,
    json={
        "ID": bookId
    },
    headers={
        "Content-Type": "application/json"
    }
)
# print(response_delete.status_code)
assert response_delete.status_code == 200
delete_response_json = response_delete.json()
print(delete_response_json['msg'])
assert delete_response_json['msg'] == 'book is successfully deleted'

# Authentication
#print(getPassword())
github_response = requests.get(
    url='https://api.github.com/user', # Need to create account in git
    auth=('sureshaboutula', 'Suresh@2789')
)
print(github_response.status_code)
print(github_response.text)

githubaccount_response = requests.get(
url='https://api.github.com/users', # Need to create account in git
    auth=('sureshaboutula', 'Suresh@2789')
)
print(githubaccount_response.status_code)
print(githubaccount_response.json()[0])
#print(len(githubaccount_response.json()))

githubrepos_response = requests.get(
url='https://api.github.com/user/repos',
    auth=('sureshaboutula', 'Suresh@2789')
)
print(githubrepos_response.status_code)