import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_50334.xml'

uh = urllib.request.urlopen(serviceurl)
data = uh.read()
tree = ET.fromstring(data)
count_sum = 0
counts = tree.findall('.//count')
print('Size of Counts =', len(counts))
print(counts)
for value in counts:
	count_value = value.text
	#print(count_value)
	count_sum = count_sum + int(count_value)
	
print(count_sum)

