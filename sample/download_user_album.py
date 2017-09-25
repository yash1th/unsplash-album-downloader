import requests
import sys
import json
import shutil
import math
import os
import argparse

BASE_URL = 'https://api.unsplash.com/users/'
HEADS = {'Accept-Version':'v1'}
APP_ID = 'c2ad675f880d50e5caf6e798af382889339186ce870798912b9cd4404b9a2b63' #put your application id here
MODE_LIST= {'w':'raw','f':'full','r':'regular','s':'small','t':'thumb'}

def parse_args():

	parser = argparse.ArgumentParser(description = 'arguments of how to download photos')
	parser.add_argument('username', type = str, help = 'username to download photos')
	parser.add_argument('-a','--albumtype', type = str, choices = ['u','U','l','L'], default = 'u', help = 'type of photos to download')
	parser.add_argument('-m','--mode',type=str,choices = ['w','f','r','s','t','W','F','R','S','T'], default = 'f')
	args = parser.parse_args()
	return args

def get_response(url, payload):
	r = requests.get(url,params = payload, headers = HEADS)
	# if r.status_code == 200 and r.text:
	data = json.loads(r.content.decode('utf-8'))
	return data, r.status_code
	# else:
	# 	# print('no response at all')
	# 	# print('system exiting')
	# 	# sys.exit()
	# 	pass


def get_user(username):
	user_profile, status_code = get_response(BASE_URL+username,{'client_id':APP_ID})
	if status_code != 200:
		print(status_code,'- user not found',sep = ' ')
		sys.exit()
	else:
	    return user_profile

def get_user_uploads(username, mode):
	user_profile = get_user(username)
	photo_ids = get_photo_ids(BASE_URL+username+'/photos/', user_profile['total_photos'],mode)
	save_photos(photo_ids, user_profile['name'],'uploads-',mode)


def get_photo_ids(url, total, mode):
	if total == 0:
		print('no photos to download')
		sys.exit()
	total_pages = math.ceil(total/30)
	photo_ids = dict()
	for page_number in range(1,total_pages+1):
		payload1 = {'client_id':APP_ID,'page':str(page_number),'per_page':'30'}
		user_photos_list_response, status_code = get_response(url,payload1)
		for i in user_photos_list_response:
			photo_ids[i['id']] = i['urls'][mode]
	return photo_ids


def get_user_likes(username, mode):
	user_profile = get_user(username)
	photo_ids = get_photo_ids(BASE_URL+username+'/likes/', user_profile['total_likes'],mode)
	save_photos(photo_ids, user_profile['name'],'likes-',mode)


def save_photos(photo_ids, name, album_type, mode):
	user_directory = os.getcwd()+r'/'+name+'-unsplash-'+album_type+mode
	if not os.path.exists(user_directory):
		os.makedirs(user_directory)
	else:
		photo_ids_local = {f[:-4] for f in os.listdir(user_directory) if f.endswith('.jpg')}
		for pid in photo_ids_local:
			try:
				del photo_ids[pid]
			except KeyError:
				print('no photo exists with the ID "{}" in unsplash'.format(pid))

	for k,v in photo_ids.items():
		photo_download_response = requests.get(photo_ids[k],stream = True)
		with open(user_directory+r'/'+k+'.jpg', 'wb') as out_file:
		    shutil.copyfileobj(photo_download_response.raw, out_file)

	print('successfully downloaded {} photos in {} format'.format(len(photo_ids),mode))

# def get_user_likes(username, mode):
# 	page_num = 1
# 	l_payload = {'client_id':app_id,'page':str(page_num),'per_page':'30'}
# 	r,s = get_response(base_url+username+'/likes',l_payload,heads)
# 	photo_ids = dict()
# 	while s == 200 and r:
# 		for i in r:
# 			photo_ids[i['id']] = i['urls'][mode]
# 		page_num += 1
# 		l_payload['page'] = str(page_num)
# 		r,s = get_response(base_url+username+'/likes',l_payload,heads)
# 	save_photos(photo_ids, 'Brooke Lark',mode)
# if r.status_code == 200 and r.text: #need to include this line to check for empty json object (Still a response with 200 code)


if __name__ == '__main__':
	args = parse_args()
	if (args.albumtype).lower() == 'u':
		get_user_uploads(args.username, MODE_LIST[(args.mode).lower()])
	if (args.albumtype).lower() == 'l':
		get_user_likes(args.username, MODE_LIST[(args.mode).lower()])
