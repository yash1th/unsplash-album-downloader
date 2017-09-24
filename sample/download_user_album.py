import requests
import sys
import json
import shutil
import math
import os
import argparse

base_url = 'https://api.unsplash.com/'
heads = {'Accept-Version':'v1'}
app_id = 'b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a'

def parse_args():

	parser = argparse.ArgumentParser(description = 'arguments of how to download photos')
	#group_photos_type = parser.add_mutually_exclusive_group()
	# group_photos_type.add_argument('-p','--photos',)
	# parser.add_argument('pt', default = 'p',choices = [p, l, c], help='type of photo collection you want to download')
	#group_photos_type.add_argument('-up', action = 'store_true', help = 'type of photo collection you want to download')
	parser.add_argument('username', type = str, help = 'username to download photos')
	group_photo_mode = parser.add_mutually_exclusive_group(required = True)
	group_photo_mode.add_argument('-w','--raw',action = 'store_true', help = 'to download raw images')
	group_photo_mode.add_argument('-f','--full',action = 'store_true', help = 'to download full size images')
	group_photo_mode.add_argument('-r','--regular',action = 'store_true', help = 'to download regular size images')
	group_photo_mode.add_argument('-s','--small',action = 'store_true', help = 'to download small size images')
	group_photo_mode.add_argument('-t','--thumb',action = 'store_true', help = 'to download thumb size images')
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

def get_user_uploads(args,mode):
    user_profile = get_user(args.username)
    photo_ids = get_photo_ids(args.username, user_profile['total_photos'],mode)
    save_photos(photo_ids, user_profile['first_name']+' '+user_profile['last_name'],mode)


def save_photos(photo_ids, name,mode):
    user_directory = os.getcwd()+r'/'+name+'-unsplash-uploads-'+mode
    #print('path = ',user_directory)
    #sys.exit()
    if not os.path.exists(user_directory):
        os.makedirs(user_directory)
    else:
        pass

    for k,v in photo_ids.items():
        photo_download_response = requests.get(photo_ids[k],stream = True)
        with open(user_directory+r'/'+k+'.jpg', 'wb') as out_file:
            shutil.copyfileobj(photo_download_response.raw, out_file)


def get_photo_ids(username, total_photos,mode):
    total_pages = math.ceil(total_photos/30)
    photo_ids = dict()
    for page_number in range(1,total_pages+1):
        payload1 = {'client_id':app_id,'page':str(page_number),'per_page':'30'}
        user_photos_list_response, status_code = get_response(base_url+'users/'+username+'/photos/',payload1,heads)
        print('mode = ',mode)
        for i in user_photos_list_response:
            photo_ids[i['id']] = i['urls'][mode]
    for k,v in photo_ids.items():
        print(v)
    return photo_ids


if __name__ == '__main__':
    args = parse_args()
    print('mode in main = ',args.small)
    mode = 'raw'
    if args.raw == True:
        mode = 'raw'
    elif args.full == True:
        mode = 'full'
    elif args.regular == True:
        mode = 'regular'
    elif args.small == True:
        mode = 'small'
    elif args.thumb == True:
        mode = 'thumb'
    else:
        sys.exit()

    get_user_uploads(args,mode)
