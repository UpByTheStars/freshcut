import os
import json
import requests

def upload_image(path, bearer=None, id=None):
	if bearer == None and id != None:
		return 'error'
	if id == None and bearer != None:
		return 'error'

	if path.split('.')[-1] not in ['jpg', 'jpeg', 'png']:
		return 'error'




def upload_video(path, bearer, id=None):
	if bearer == None and id != None:
		return 'error'
	if id == None and bearer != None:
		return 'error'

	if path.split('.')[-1] not in ['mp4']:
		return 'error'

	if bearer.split(' ')[0] != 'Bearer':
		bearer = 'Bearer', bearer 
	
	headers = {'authorization': str(bearer)}
	
	x = requests.post(f'https://clips-v1-api-z5giai34ua-uc.a.run.app/users/{id}/clips', json={"sourceType":"USER_FILE"}, headers=headers)
	if x.status_code == 401:
		return 'Invalid authentication'

	x = json.loads(x.text)
	uploadURL = x["data"]["uploadUrl"]
	vid_id = x["data"]["id"]

				
	payload = {"query":"mutation ($v1:String!,$v2:DraftVideoPostInput!){userUploads(userId:$v1){createDraftVideoPost(input:$v2){...f1}}},fragment f1 on CreatePostResult{postId,__typename}","variables":{"v1":str(id),"v2":{"clipId":str(vid_id)}}}
	
	r = requests.post('https://graphql-gateway-z5giai34ua-uc.a.run.app/', headers=headers, json=payload)
	vid_id = json.loads((r.text))["data"]["userUploads"]["createDraftVideoPost"]["postId"]

	with open(path, "rb") as video_file:
		response = requests.put(uploadURL, data=video_file, headers={'host': 'us-east-1-779278615482-clips.s3-accelerate.amazonaws.com', 'Content-Type': 'video/mp4'})
	if response.status_code != 200:
		return 'Error: ' + response.status_code
	return True, vid_id




def post(bearer, post_id, video_name, community_id, thumbnail_url, id=None):
	if bearer.split(' ')[0] != 'Bearer':
		bearer = 'Bearer', bearer 
	
	headers = {'authorization': str(bearer)}

	try:
	
		x = requests.post('https://graphql-gateway-z5giai34ua-uc.a.run.app/', headers=headers, json={"query":"mutation ($v1:String!,$v2:String!,$v3:UpdatePostInput!){userUploads(userId:$v1){updatePost(postId:$v2,opts:$v3){...f1}}},fragment f1 on Void{void,__typename}","variables":{"v1":str(id),"v2":str(id),"v3":{"thumbnailUrl":str(thumbnail_url),"description":str(video_name),"communityId":str(community_id),"tagIds":[]}}})
			
			
		x = requests.post('https://graphql-gateway-z5giai34ua-uc.a.run.app/', headers=headers, json={"query":"mutation ($v1:String!,$v2:String!){userUploads(userId:$v1){publishPost(postId:$v2){...f1}}},fragment f1 on Void{void,__typename}","variables":{"v1":str(id),"v2":str(post_id)}})
	except:
		return False

	return True