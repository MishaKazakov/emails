import re
import requests

emails = set()
urls = set()

def findAllEmails(page):
    res = re.findall('[^"\'>:<\- ]+@[^"\'>:<\- ]+', page.text)
    for word in res:
        emails.add(word.__str__())

def findNewUrl(url,mainSite):
    site = requests.get(url)    
    findAllEmails(site)
    findNewUrl.counter
    slash = unicode('/')
    res = re.findall('<a href="('+ mainSite + '[^"\'>.]*)', site.text)
    rel = re.findall('<a href="/([^ "\'>]+)', site.text)
    for adress in rel:
        if adress[0] == slash:
            res.append('https://' + adress[1:])
        else:
            res.append(mainSite + adress)
    for adress in res:
        if findNewUrl.counter < 10:
            if not re.search('files', adress):
                if not urls.__contains__(adress) :
                    urls.add(adress)
                    print(findNewUrl.counter ,adress)
                    findNewUrl.counter +=1
                    findNewUrl(adress, mainSite)
       

a = unicode('http://www.mosigra.ru/' )
urls.add(a)
findNewUrl.counter = 0
findNewUrl(a,a)

for email in emails:
    print(email)
