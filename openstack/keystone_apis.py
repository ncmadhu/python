# Date: 12-07-2017
# Author: Madhu Chakravarthy

import json
import rest_client

def keystone_auth(controller, user, password):

    url = "http://{0}:{1}{2}".format(controller, "35357", "/v3/auth/tokens")

    request_json = {
                        "auth": {
                            "identity": {
                                "methods": [
                                    "password"
                                 ],
                                 "password": {
                                     "user": {
                                         "name": user,
                                         "domain": {
                                             "name": "Default"
                                         },
                                         "password": password
                                     }
                                 }
                            },
                            "scope": {
                                "project":   {
                                    "name": "admin",
                                    "domain": {
                                        "id": "default",
                                        "name": "Default"
                                    }
                                }
                            }
                        }
                   }

    result, response = rest_client.post_request(url, request_json)

    if result == "success":
        token_id = response.headers['X-Subject-Token']
        return result, token_id
    else:
        error = json.loads(response.content)['error']['message']
        return result, error


def keystone_catalog(controller, token):

    url = "http://{0}:{1}{2}".format(controller, "35357", "/v3/auth/catalog")
    headers = {"Accept-Type": "application/json", "X-Auth-Token": token}

    result, response = rest_client.get_request(url, headers=headers)

    if result == "success":
        catalog = json.loads(response.content)['catalog']
        return result, catalog 
    else:
        error = json.loads(response.content)['error']['message']
        return result, error
    


if __name__ == "__main__":

    result, response = keystone_auth("10.1.4.205", "admin", "calsoftlabs@2017")
    print response
    if result == "success":
        token = response
    else:
        token = None

    if token:
        result, response = keystone_catalog("10.1.4.205", token)
        print response


