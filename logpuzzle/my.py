import re
import sys
import urllib.request
import os
filename = 'apple-cat.ru_access.log'
#f = open('babynames_boys.html','r',encoding = "utf-8")
try:
    f = open(filename,'r',encoding = "utf-8")
except FileNotFoundError:
    sys.exit(1)
text = f.read()
reg = re.compile(r'GET /images/(.*?) HTTP/1.1', re.DOTALL)	
im = []
for x in reg.findall(text):
    if x not in im:
        im.append(x)
#print(sorted(im))
#for x in im:
#    urllib.request.urlretrieve('http://apple-cat.ru/images/'+x,x)
#print(os.listdir('/'))
dest_dir = 'img'
if os.path.exists(dest_dir):
    a=1
else:
    os.makedirs(dest_dir)
#print(os.listdir())
myurls=[]
for x in im:
    urllib.request.urlretrieve('http://apple-cat.ru/images/'+x,dest_dir+'/img'+x[-6:])
    myurls.append(dest_dir + '/img'+x[-6:])
#print (myurls)
f=open('index.html','w+')
f.writelines(['<html>','<body>'])
for x in sorted(myurls):
    f.write('<img src="'+ x + '">')
f.writelines(['</body>','</html>'])
