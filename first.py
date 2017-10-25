import re
import requests

emails = set()
urls = set()

def findAllEmails(page):
    res = re.findall('\w+@\w+.\w+', page.text)
    for word in res:
        emails.add(word.__str__())

def findNewUrl(url):
    site = requests.get(url)    
    findAllEmails(site)
    res = re.findall('<a href="(http://www.csd.tsu.ru/[^"\'>.]*)', site.text)   
    for adress in res:
        if not re.search('files', adress):
            if not urls.__contains__(adress) :
                urls.add(adress)
                #print(findNewUrl.counter ,adress)
                findNewUrl.counter +=1
                findNewUrl(adress)

a = unicode('http://www.csd.tsu.ru/' )
urls.add(a)
findNewUrl.counter = 0
findNewUrl(a)

for email in emails:
    print(email)
