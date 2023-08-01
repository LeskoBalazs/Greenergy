import requests

url = 'http://127.0.0.1:8000/swap'
test_input = input()
data = {'string': test_input}
response = requests.post(url, data=data)

if response.status_code == 200:
    print(response.json()['result'])
else:
    print(response.json()['error'])
