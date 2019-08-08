# Date: 12-07-2017
# Author: Madhu Chakravarthy

import json
import requests

headers = {"Content-Type":"application/json", "Accept-Type": "application/json"}


def post_request(url, data, headers=headers):


    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        result = "success"
    else:
        result = "fail"

    return result, response


def get_request(url, headers=headers):

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = "success"
    else:
        result = "fail"

    return result, response

