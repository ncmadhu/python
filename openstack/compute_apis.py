# Date: 12-07-2017
# Author: Madhu Chakravarthy

import json

import rest_client
import keystone_apis

def servers_list(controller, token):

    url = "http://{0}:{1}{2}".format(controller, "8774", "/v2.1/servers")
    headers = {"Accept-Type": "application/json", "X-Auth-Token": token}

    result, response =  rest_client.get_request(url, headers=headers)

    if result == "success":
        catalog = json.loads(response.content)['servers']
        return result, catalog
    else:
        error = json.loads(response.content)['error']['message']
        return result, error

if __name__ == "__main__":

    result, response = keystone_apis.keystone_auth("10.1.4.205", "admin", "calsoftlabs@2017")
    print response
    if result == "success":
        token = response
    else:
        token = None

    if token:
        result, response = servers_list("10.1.4.205", token)
        print response


