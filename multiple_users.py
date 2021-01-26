# https://randomuser.me/api/?results=5000

import requests
users_count = '600'

url = f'https://randomuser.me/api/?results={users_count}'

response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()
    f = open('randomuser/multiple_users.json', 'w')
    f.write(str(response_json))
    f.close
elif response.status_code == 404:
    print('Not found')