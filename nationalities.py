# https://randomuser.me/api/?nat=gb
# https://randomuser.me/api/?nat=us,dk,fr,gb

import requests

nat_only = 'gb'
nat_many = 'us,dk,fr,gb'
url_only = f'https://randomuser.me/api/?nat={nat_only}'
url_many = f'https://randomuser.me/api/?nat={nat_many}'


# Bitta millat vakili buyicha
response_only = requests.get(url_only)
if response_only.status_code == 200:
    response_only_json = response_only.json()
    f = open('randomuser/nat_only.json', 'w')
    f.write(str(response_only_json))
    f.close
elif response_only.status_code == 404:
    print('Not found')

# Bir qancha millatlar vakili buyicha
response_many = requests.get(url_many)
if response_many.status_code == 200:
    response_many_json = response_many.json()
    f = open('randomuser/nat_many.json', 'w')
    f.write(str(response_many_json))
    f.close
elif response_many.status_code == 404:
    print('Not found')