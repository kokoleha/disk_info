import requests

url = 'http://localhost:8000'
response = requests.get(url)
if response:
    print('Success!')
else:
    print('An error has occurred.')











