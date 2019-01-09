import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def Retrieve(url, position):
	print('Retrieving:', url)
	# Ignore SSL certificate errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	if (len(tags)) > 0:
		tag = tags[position]
		return tag.get('href', None)



url_base = input('Enter URL: ')
scount = input('Enter Count: ')
icount = int(scount)
sposition = input('Enter Position: ')
iposition = int(sposition)

while (icount >= 0):
	url_base = Retrieve(url_base, iposition - 1)
	icount = icount - 1



# Retrieve all of the anchor tags

	

#http://py4e-data.dr-chuck.net/known_by_Fikret.html	