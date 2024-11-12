
import requests
import json

import utilities
from payload import *
from utilities.configurations import *
from utilities.resources import *

def after_scenario(context, scenario):
    if "library" in scenario.tags:
        response_delete = requests.post(
            url=getConfig()['API']['endpoint'] + ApiResources.deleteBook,
            json={
                "ID": context.bookId
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