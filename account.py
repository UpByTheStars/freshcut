import os
import json
import requests

def create_account(email, password):
	x = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDZf-9-dXoyqYZDupgQUfcwd9pHLReqMrY', json={"returnSecureToken":True,"email":email,"password":password,"clientType":"CLIENT_TYPE_WEB"})

	token = (json.loads(str(x.text)))["idToken"]
	local_id = (json.loads(str(x.text)))["localId"]
	
	return token, local_id