import requests

url = 'http://127.0.0.1:5000/debate'
data = {'user_input': 'I believe doing exercise daily makes us healthy.'}

response = requests.post(url, json=data)
print(response.json())
