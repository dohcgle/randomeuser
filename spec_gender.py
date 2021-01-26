# https://randomuser.me/api/?gender=female

import requests
gender = 'male'
url = f'https://randomuser.me/api/?gender={gender}'

response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()
    f = open('randomuser/spec_gender.json', 'w')
    f.write(str(response_json))    
    f.close
elif response.status_code == 404:
    print('Not found')

