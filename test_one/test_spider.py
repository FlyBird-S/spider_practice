import re,urllib2
req = urllib2.urlopen('https://www.imooc.com/')
buf = req.read()
listurl = re.findall(r'src="//.+?\.jpg',buf)
listurl = [i.replace('src="','http:') for i in listurl] #lsit exchange
listurl = set(listurl)# remove repeat
print listurl
i=0
for url in listurl:
    f = open("C:\\Users\\aff\\Desktop\\python\\" +"test"+ str(i)+'.jpg','wb')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i+=1
print "OK"

