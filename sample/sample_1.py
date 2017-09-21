import requests
import sys
import json


url = 'https://api.unsplash.com/'
heads = {'Accept-Version':'v1'}
app_id = 'b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a'
payload = {'client_id':app_id,'per_page':'57'}
r = requests.get(url+'/users/'+sys.argv[1]+'/photos',params = payload, headers = heads)
print('url = ',r.url)
print('response code = ',r.status_code)
# print('response content = ',r.content)
c = r.content
my_json = c.decode('utf-8')

print(type(my_json))
print(len(my_json))

data = json.loads(my_json)
print(json.dumps(data,indent=4))
photo_ids = dict()
for photo in data:
    photo_ids[photo['id']] = photo['urls']['full']

print('\n\n')
print(photo_ids)

import shutil

for k,v in photo_ids.items():
    final_response = requests.get(photo_ids[k], stream=True)
    with open(k+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(final_response.raw, out_file)

# for pid in photo_ids:
#     url_p =url+'/photos/'
#     p = requests.get(url_p+pid+'/download',params = {'client_id':app_id},headers = heads)
#     # final_url = p.content.decode('utf-8')[8:-2]
#     # final_response = requests.get(final_url, stream=True)
#     # with open(pid+'.jpg', 'wb') as out_file:
#     #     shutil.copyfileobj(response.raw, out_file)
#     # del final_response
#     # break

print('program execution done')
# for i in data:
#     for k,v in data[i].items():
#         print(k['id'])


#print(json.dumps(data,indent = 4))





#print(r.content.decode('utf-8'))

#
# r = requests.get('https://api.unsplash.com/users/andrewtneel/?client_id='+'b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a')
# print(r.status_code)
# print(r.url)

#https://api.unsplash.com/users/andrewtneel/?client_id=b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a
#curl https://api.unsplash.com/users/andrewtneel/\?client_id\=b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a
