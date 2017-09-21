import requests
import sys
import json
import shutil
import math
import os

base_url = 'https://api.unsplash.com/'
heads = {'Accept-Version':'v1'}
app_id = 'b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a'
payload1 = {'client_id':app_id}
username = sys.argv[1]
user_profile_response = requests.get(base_url+'users/'+username,params = payload1, headers = heads)
user_profile_response = json.loads(user_profile_response.content.decode('utf-8'))
user_total_photos = user_profile_response['total_photos']
user_fullname = user_profile_response['first_name']+' '+user_profile_response['last_name']
total_pages = math.ceil(user_total_photos/30)


photo_ids = dict()
for page_number in range(1,total_pages+1):
    payload2 = {'client_id':app_id,'page':str(page_number),'per_page':'30'}
    user_photos_list_response = requests.get(base_url+'users/'+username+'/photos/',params = payload2,headers = heads)
    user_photos_list_response = json.loads(user_photos_list_response.content.decode('utf-8'))
    for i in user_photos_list_response:
        photo_ids[i['id']] = i['urls']['full']

user_directory = os.getcwd()+r'/'+user_fullname+'-unsplash'
if not os.path.exists(user_directory):
    os.makedirs(user_directory)

for k,v in photo_ids.items():
    photo_download_response = requests.get(photo_ids[k],stream = True)
    with open(user_directory+r'/'+k+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(photo_download_response.raw, out_file)
