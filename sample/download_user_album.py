import requests
import sys
import json
import shutil
import math
import os
import argparse

base_url = 'https://api.unsplash.com/'
heads = {'Accept-Version':'v1'}
app_id = '' #put your app id here
mode_list= {'w':'raw','f':'full','r':'regular','s':'small','t':'thumb'}

def parse_args():

	parser = argparse.ArgumentParser(description = 'arguments of how to download photos')
	parser.add_argument('username', type = str, help = 'username to download photos')
	parser.add_argument('-m','--mode',type=str,choices = ['w','f','r','s','t','W','F','R','S','T'], default = 'f')
	args = parser.parse_args()
	return args

def get_response(url, payload, heads):
    r = requests.get(url,params = payload, headers = heads)
    data = json.loads(r.content.decode('utf-8'))
    return data, r.status_code

def get_user(username):
    user_profile, status_code = get_response(base_url+'users/'+username,{'client_id':app_id},heads)
    if status_code != 200:
        print(status_code,'- user not found',sep = ' ')
        sys.exit()
    else:
        return user_profile

def get_user_uploads(username, mode):
	user_profile = get_user(username)
	photo_ids = get_photo_ids(args.username, user_profile['total_photos'],mode)
	save_photos(photo_ids, user_profile['first_name']+' '+user_profile['last_name'],mode)


def save_photos(photo_ids, name, mode):
	user_directory = os.getcwd()+r'/'+name+'-unsplash-uploads-'+mode
	if not os.path.exists(user_directory):
		os.makedirs(user_directory)
	else:
		photo_ids_local = {f[:-4] for f in os.listdir(user_directory) if f.endswith('.jpg')}
		for pid in photo_ids_local:
			try:
				del photo_ids[pid]
				#print('deleted {} for requesting'.format(pid))
			except KeyError:
				print('no photo exists with the ID "{}" in unsplash'.format(pid))

	for k,v in photo_ids.items():
		photo_download_response = requests.get(photo_ids[k],stream = True)
		with open(user_directory+r'/'+k+'.jpg', 'wb') as out_file:
		    shutil.copyfileobj(photo_download_response.raw, out_file)

	print('successfully downloaded {} photos in {} format'.format(len(photo_ids),mode))


def get_photo_ids(username, total_photos, mode):
    total_pages = math.ceil(total_photos/30)
    photo_ids = dict()
    for page_number in range(1,total_pages+1):
        payload1 = {'client_id':app_id,'page':str(page_number),'per_page':'30'}
        user_photos_list_response, status_code = get_response(base_url+'users/'+username+'/photos/',payload1,heads)
        for i in user_photos_list_response:
            photo_ids[i['id']] = i['urls'][mode]
    return photo_ids


if __name__ == '__main__':
	args = parse_args()
	get_user_uploads(args.username, mode_list[(args.mode).lower()])
