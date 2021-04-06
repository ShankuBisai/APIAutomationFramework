import requests
from configs.hosts_config import API_HOSTS
from utilities.credentialUtility import CredentialsUtility
import os
from requests_oauthlib import OAuth1
import json

class RequestUtlity(object):
    def __init__(self):

        self.env = os.environ.get("ENV")
        self.baseURL = API_HOSTS[self.env]
        self.auth = OAuth1(CredentialsUtility.getWCAPIKeys()["wcKey"],CredentialsUtility.getWCAPIKeys()["wcSecret"])

    def post(self,endpoint,payload,header=None):
        if not header:
            headers = {"Content-Type":"application/json"}
        url = self.baseURL+endpoint
        response = requests.post(url = url,data=json.dumps(payload),headers=headers,auth = self.auth)
        return response

    def get(self,endpoint,header=None,payload = None):
        if not header:
            headers = {"Content-Type": "application/json"}
        url = self.baseURL + endpoint
        response = requests.get(url=url,data = json.dumps(payload),headers=headers, auth=self.auth)
        return response
