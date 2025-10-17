import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

import requests

url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
query = 'select * from books'
addBook_response = requests.post(url, json=buildPayLoadfromDB(query), headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)
# Delete Book -
url2 = getConfig()['API']['endpoint'] + ApiResources.deleteBook

response_deleteBook = requests.post(url2, json={

    "ID": bookId
}, headers=headers, )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

# Authentication
url3 = "https://api.github.com/user/repos"
token = getPassword()  # make sure this returns your token, not password
github_response = requests.get(url3, headers={"Authorization": f"token {token}"})

print(github_response.status_code)
