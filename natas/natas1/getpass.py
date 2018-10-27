import requests
import re

user = "natas1"
pwd = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

url = 'http://%s.natas.labs.overthewire.org/' % user
session = requests.Session()

response = session.get(url, auth=(user,pwd))
content = response.text


print(re.findall('<!--The password for natas2 is (.*) -->',content)[0])