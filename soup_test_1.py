import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
value_sum = 0
tags = soup('span')
for tag in tags:
    #print('Tag:', tag)
    #print('Contents', tag.contents[0])
    value_sum = value_sum + int(tag.contents[0])

print(value_sum)