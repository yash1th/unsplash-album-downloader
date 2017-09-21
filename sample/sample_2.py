import requests
import sys
import json
import math

api_url = 'https://api.unsplash.com/users/'
heads = {'Accept-Version':'v1'}
app_id = 'b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a'
payload1 = {'client_id':app_id}
user_resp = requests.get(api_url+sys.argv[1],params = payload1, headers = heads)
print('url = ',user_resp.url)
print('user_profile.response code = ',user_resp.status_code)
user_resp_dict = json.loads(user_resp.content.decode('utf-8'))
user_total_photos = user_resp_dict['total_photos']
user_photos_url = user_resp_dict['links']['photos']
user_fullname = user_resp_dict['name']
total_pages = math.ceil(user_total_photos/30)

photo_ids = []
for i in range(1, total_pages+1):
    payload2 = {'client_id':app_id,'page':str(i),'per_page':'30'}
    r = requests.get(user_photos_url,params = payload2, headers = heads)
    print('url = ',r.url)
    print('response code = ',r.status_code)
    data = json.loads(r.content.decode('utf-8'))
    for photo in data:
          photo_ids.append(photo['id'])


# print(len(photo_ids))
# print('\n\n\n\n\n\n')
# print(photo_ids)




# print('tp : ',user_total_photos)
# print('photos url : ',user_photos_link)
# print('full name :',user_fullname)
