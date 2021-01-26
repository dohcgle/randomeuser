# https://randomuser.me/api/?inc=gender,name,nat

import requests
url = 'https://randomuser.me/api/?inc=gender,name,nat'
response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()
    f = open('randomuser/inc.json', 'w')
    f.write(str(response_json))
    f.close
elif response.status_code == 404:
    print('Not found')