#!/usr/bin/python3
print("Content-type:text/html \n\n")

import mysql.connector
from mysql.connector import Error
import base64
from urllib.request import urlopen
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.apple.com/mac/"
uREQ = urlopen(url)
pageC = uREQ.read()
uREQ.close()
soup = BeautifulSoup(pageC,"html.parser")
# print(soup.prettify())

file=open("project.csv","w")
# print("<head><link rel='stylesheet' href='project.css'></head>")
# print("<body id='box1'><link rel='stylesheet' href='project.css'></body>")
print(soup.title)

print("<h1 id='box2'>")
titles = soup.find("h2",{'class':"typography-headline-elevated headline-elevated large-8 small-12 large-centered text-center"})
print(titles.string.encode("ascii", errors="xmlcharrefreplace").decode())
file.write(titles.string.encode("ascii", errors="ignore").decode()+"\n")
print("</h1>")

print("<table border=1>")
print("<tr class='box3'>")
models = soup.find_all("h3",{'class':"compare-headline typography-compare-headline"})
for a in models:
    print("<td>","<b>",a.getText().encode("ascii", errors="xmlcharrefreplace").decode(),"<b>","</td>")
print("</tr>")

print("<tr>")
prices = soup.find_all("p",{'class':"typography-body-reduced copy-pricing"})
for b in prices:
    print("<td>",b.string.encode("ascii", errors="xmlcharrefreplace").decode(),"</td>")
print("</tr>")

print("<tr>")
display = soup.find_all("ul",{'class':"feature-list list list-nobullet typography-body-reduced"})
for c in display:
    print("<td>",c.find_all('li')[0].getText().encode("ascii", errors="xmlcharrefreplace").decode(),"</td>")
print("</tr>")

print("<tr>")
memory = soup.find_all("ul",{'class':"feature-list list list-nobullet typography-body-reduced"})
for d in memory:
    print("<td>",d.find_all('li')[2].getText().encode("ascii", errors="xmlcharrefreplace").decode(),"</td>")
print("</tr>")

print("<tr>")
processor = soup.find_all("ul",{'class':"feature-list list list-nobullet typography-body-reduced"})
for e in processor:
    print("<td>",e.find_all('li')[1].getText().encode("ascii", errors="xmlcharrefreplace").decode(),"</td>")
print("</tr>")

print("<tr>")
storage = soup.find_all("ul",{'class':"feature-list list list-nobullet typography-body-reduced"})
for f in storage:
    print("<td>",f.find_all('li')[3].getText().encode("ascii", errors="xmlcharrefreplace").decode(),"</td>")
print("</tr>")

print("<tr>")
batterylife = soup.find_all("ul",{'class':"feature-list list list-nobullet typography-body-reduced"})
for g in batterylife:
    print("<td>",g.find_all('li')[4].getText().encode("ascii", errors="xmlcharrefreplace").decode(),"</td>")
print("</tr>")
print("</table>")

for a,b,c,d,e,f,g in zip(models,prices,display,memory,processor,storage,batterylife):
    file.write(
        a.string.encode("ascii", errors="ignore").decode()+","+
        b.string.encode("ascii", errors="xmlcharrefreplace").decode()+","+
        c.find_all('li')[0].getText().encode("ascii", errors="xmlcharrefreplace").decode()+","+
        d.find_all('li')[2].getText().encode("ascii", errors="xmlcharrefreplace").decode()+","+
        e.find_all('li')[1].getText().encode("ascii", errors="xmlcharrefreplace").decode()+","+
        f.find_all('li')[3].getText().encode("ascii", errors="xmlcharrefreplace").decode()+","+
        g.find_all('li')[4].getText().encode("ascii", errors="xmlcharrefreplace").decode()+"\n")
file.close()