import requests
base_url = 'https://api.unsplash.com/photos/users/jilebi/client_id=b2b72af949a8f7f5cddfcadcebcbbbd8981be1d99d30261ea5deebf05c7fb54a'
r = requests.get(base_url, headers = {'Accept-Version':'v1'})
print(r.status_code)
