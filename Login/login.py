import json
import requests

#登陆
def Login(username,pwd):
    url="http://127.0.0.1:80/api/mgr/loginReq"
    headers={
        "Content-Type":"application/x-www-form-urlencoded"      #data=dict
                      #"application/json"                       #data=str
    }
    # data="username={}&password={}".format(username,pwd)
    data={
        "username":username,    #默认auto
        "password":pwd  #默认sdfsdfsdf
    }
    resp=requests.post(url,headers=headers,data=data)
    return json.loads(resp.text)
