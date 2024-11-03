import json

import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'}
             )

# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response[0]['isbn'])
json_response = response.json()
print(type(json_response))
#print(response.json())
print(json_response[0]['isbn'])
assert response.status_code == 200
#print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
#print(response.cookies)

# Retrieve the book details with isbn RS49
for actualBook in json_response:
    if actualBook['isbn'] == 'RS49':
        print(actualBook)
        break

expectedBook = {
  "book_name": "Learn Appium Automation with Java",
  "isbn": "RS49",
  "aisle": "269"
}

assert actualBook == expectedBook