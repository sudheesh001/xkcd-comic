import urllib
from bs4 import BeautifulSoup
import requests
import shutil
#404, 838,353 fail.
for x in range(1,1302):
	url = 'http://www.xkcd.com/'+str(x)+'/'
	f = urllib.urlopen(url)
	txt = f.read();
	title_pos1 = txt.find(b'<title>')
	title_pos2 = txt.find(b'</title>')
	#fetching title
	title = txt[title_pos1:title_pos2]
	title = title.replace('<title>','')
	#replacing the xkcd: from title
	title = title.replace('xkcd: ', '')
	img_search = 'alt="' + (title);
	#finding nearest alt to the actual link to the image
	altfind = txt.find(img_search)
	txt = txt[0:altfind]
	img_pos = txt.rfind("<img ")
	txt = txt[img_pos:altfind]
	link_pos1 = txt.find('"')
	txt = txt[link_pos1+1:altfind]
	link_pos2 = txt.find('"')
	link = txt[0:link_pos2]
	#print (link)
	#downloading video file using urllib2
	f = urllib.urlopen(link)
	file_name = (str(x)+ " . " +title +'.PNG')
	print ("downloading " + file_name)
	# Open our local file for writing
	local_file = open('./'+file_name, "w" + 'b')
	#Write to our local file
	local_file.write(f.read())
	local_file.close()

# soup = BeautifulSoup(urllib.urlopen(url).read())
# link = soup.findAll('img')[0].get('src')
# print link

# r = requests.get(link)
# with open('1.png','wb') as out_file:
# 	shutil.copyfileobj(r.raw,out_file)
# del r
