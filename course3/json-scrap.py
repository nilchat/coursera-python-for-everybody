import urllib.request
import urllib.parse
import urllib.error
import json

url = input('Enter location: ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()

js = json.loads(data)

sum = 0
for item in js["comments"]:
    sum += item["count"]
print(sum)
