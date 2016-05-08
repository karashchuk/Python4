import re
import requests
page = requests.get('http://zags.mos.ru/stat/imena/imena_malchikov.php')

print (page.text)

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
				
