import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
html = urllib.request.urlopen(url).read()
data = html.decode()

info = json.loads(data)
print('User count:', len(info["comments"]))
sum_count = 0
for item in info["comments"]:
   sum_count = sum_count + int(item['count'])
   #print(item)

print(sum_count)
    


#http://py4e-data.dr-chuck.net/comments_42.json

