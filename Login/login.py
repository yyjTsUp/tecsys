import json
import requests
from const import consts

#登陆
def Login(username,pwd):
    url=consts.domain+consts.login_url
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

if __name__=="__main__":
    print(Login('auto','sdfsdfsdf'))


