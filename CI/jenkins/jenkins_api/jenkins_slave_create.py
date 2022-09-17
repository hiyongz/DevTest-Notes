import json
import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

params = (
    ('name', 'test_sep17_TBR'),
    ('type', 'hudson.slaves.DumbSlave'),
)

# postdata = open('my_file.json', 'rb').read()

with open('my_file.json', 'r') as load_f:
    postdata = json.load(load_f)

url = 'http://zhanghaiyong:11c0e9b635a438ffc401ac2752a13d4950@192.168.168.228:8080/computer/doCreateItem?name=win_98.172&type=hudson.slaves.DumbSlave'
response = requests.post(url, data=f'json={json.dumps(postdata)}', headers=headers)
print(response.text)