import os
import json
import requests

def create_account(email, password):
	x = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDZf-9-dXoyqYZDupgQUfcwd9pHLReqMrY', json={"returnSecureToken":True,"email":email,"password":password,"clientType":"CLIENT_TYPE_WEB"})

	token = (json.loads(str(x.text)))["idToken"]
	local_id = (json.loads(str(x.text)))["localId"]
	
	return token, local_id

def get_gems(bearer, id):

	if bearer.split(' ')[0] != 'Bearer':
		bearer = 'Bearer', bearer 
	
	headers = {'authorization': str(bearer)}
	
	x = requests.post('https://graphql-gateway-z5giai34ua-uc.a.run.app/', headers=headers, json={"query":"query ($v1:String!){inventory(userId:$v1){balance{IFCD}}}","variables":{"v1":id}})

	return (json.loads(str(x.text)))["data"]["inventory"]["balance"]["IFCD"]