
import requests
import json



def getReq(url):
    response = requests.get(url)
    decode_response = json.loads(response.content)
    return decode_response

def postReq():

    url_get_token = 'http://127.0.0.1:8000/api/v1/token/'
    data = {
        'username':'bandit',
        'password':'q1w2e3r4',
    }
    response = requests.post(url_get_token,data=data)
    decode_response = json.loads(response.content)
    return decode_response['access']

def postReqTest(url):
    
    headers = {
        # "Accept": "application/json",
        'Authorization': f'AUTHTOKEN {postReq()}',
        # 'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'title':'xcvxv',
        'body':'tfertf',
    }
    response = requests.post(url,headers=headers,data=data)
    decode_response = json.loads(response.content)
    return decode_response

def postReqTest2(url):
    
    data = {
        'title':'tort',
        'body':'YaBanan17',
    }
    response = requests.post(url,data=data)
    decode_response = json.loads(response.content)
    return decode_response


url = 'http://127.0.0.1:8000/api/v1/test/'

print(getReq(url))