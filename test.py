import requests
from requests.auth import HTTPBasicAuth

post = requests.post('http://127.0.0.1:8000/time-test/', json={'ore_lavorative': 5}, auth=HTTPBasicAuth('dima', 'dima')) #'datetime_add': str(date)})

print(post)