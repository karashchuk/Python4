import re
import sys
filename = 'babynames_boys.html'
#f = open('babynames_boys.html','r',encoding = "utf-8")
try:
    f = open(filename,'r',encoding = "utf-8")
except FileNotFoundError:
    sys.exit(1)
text = f.read()

"""<tr> <td width="57"> 
					1
				</td> <td width="177"> 
					Артём, Артем 
				</td> <td width="76"> 
					3330 (4,8%)* 
				</td> <td width="90"> 
					2683 (4,2%) 
				</td> <td width="90"> 
					1996 (4,2%) 
				</td> <td width="90"> 
					1355 (3,6%) 
				</td> <td width="90"> 
					1060 (2,1%) 
				</td> </tr>"""


#reg = re.compile(r'''<tr>(.*?)</tr>''', re.DOTALL|re.VERBOSE)	
"""reg = re.compile(r'''<tr><td width="57">\s*
						(.*?)\s*
				</td> <td width="177">\s* 
					(.*?)\s*
				</td> <td width="76">\s* 
					(.*?)\s*
				</td> <td width="90">\s* 
					(.*?)\s*
				</td> <td width="90">\s*
					(.*?)\s*
				</td> <td width="90">\s*
					(.*?)\s*
				</td> <td width="90">\s*
					(.*?)\s*
				</td> </tr>''', re.DOTALL|re.VERBOSE)"""
"""reg = re.compile(r'''<td width="57">\S*
					(.*?)\S*
				</td> <td width="177">\S*
					(.*?)\S*
				</td>''', re.DOTALL)"""	
#reg = re.compile(r'''<td width="57">\s*(.*?)\s*</td> <td width="177">\s*(.*?)\s*</td> <td width="76">\s*(.*?)\s*</td> <td width="90">\s*(.*?)\s*</td> <td width="90"> \n\t\t\t\t\t(.*?)\n\t\t\t\t</td> <td width="90"> \n\t\t\t\t\t(.*?)\n\t\t\t\t</td> <td width="90"> \n\t\t\t\t\t(.*?)\n\t\t\t\t</td>''', re.DOTALL)						
reg = re.compile(r'''<td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td> <td width="\d*">\s*(.*?)\s*</td>''', re.DOTALL)
#myr=list(reg.findall(text))
#print (myr)
babynames = {}
for x in reg.findall(text):
    babynames[x[1]]=[x[2],x[3],x[4],x[5],x[6]]
cycle = 'y'
while cycle =='y':
    a = input('введите год:   ')
    if a =="2012":
        i = 0
    elif a =="2010":
        i = 1
    elif a =="2005":
        i = 2
    elif a =="2000":
        i = 3
    elif a =="1990":
        i = 4
    else :
        print ('нет такого года')
        i = 0
    for x in sorted(babynames):
        print ('{:30} {:12}'.format(x, babynames[x][i]))
    cycle = input ('Еще? (y/n):  ')
    #if c != 'y':
    #    break