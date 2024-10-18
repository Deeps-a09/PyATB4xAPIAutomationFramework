# Pre build

import json
import requests

def get_requests(url, auth):
    response = requests.put(url=url, auth= auth)
    return response.json()

def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url = url, headers= headers, auth=auth, data= json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_request_data(url, auth, headers, payload, in_json):
    patch_response_data = requests.post(url = url, headers= headers, auth=auth, data= json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data

def put_request(url, auth, headers, payload, in_json):
    put_response_data = requests.post(url = url, headers= headers, auth=auth, data= json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data

def delete_request(url, auth, headers, payload, in_json):
    delete_response_data = requests.post(url = url, headers= headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data