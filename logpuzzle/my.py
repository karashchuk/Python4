import re
import sys
filename = 'apple-cat.ru_access.log'
#f = open('babynames_boys.html','r',encoding = "utf-8")
try:
    f = open(filename,'r',encoding = "utf-8")
except FileNotFoundError:
    sys.exit(1)
text = f.read()


reg = re.compile(r'GET /images/(.*?) HTTP/1.1', re.DOTALL)	

#reg = re.compile(r'''<td width="57">\s*(.*?)\s*</td> <td width="177">\s*(.*?)\s*</td> <td width="76">\s*(.*?)\s*</td> <td width="90">\s*(.*?)\s*</td> <td width="90"> \n\t\t\t\t\t(.*?)\n\t\t\t\t</td> <td width="90"> \n\t\t\t\t\t(.*?)\n\t\t\t\t</td> <td width="90"> \n\t\t\t\t\t(.*?)\n\t\t\t\t</td>''', re.DOTALL)						
#reg = re.compile(r'''<td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td>''', re.DOTALL)
#myr=list(reg.findall(text))
#print (myr)
im = []
for x in reg.findall(text):
    print (x)
    if x not in im:
    #else:
        im.append(x)
print(sorted(im))
