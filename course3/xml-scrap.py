import urllib.request as ureq
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
raw_data = ureq.urlopen(url, context=ctx).read()

tree = ET.fromstring(raw_data)
lst = tree.findall('comments/comment')
sum = 0
for item in lst:
    sum += int(item.find('count').text)
print(sum)
