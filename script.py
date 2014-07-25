from bs4 import BeautifulSoup
import urllib


source = raw_input('paste your 4chan thread here\n');
source = urllib.urlopen(source)
soup = BeautifulSoup(source)


elements = soup.find_all("a", class_="fileThumb")

urls = []

for x in elements:
	strng = x.get('href')
	strng = strng[2:]
	urls.append(strng)

src = raw_input('paste the folder source youd like to download your images to here\n');

for j in urls:
	urllib.urlretrieve('http://' + j, src + "\%s.jpg" % (urls.index(j)))

