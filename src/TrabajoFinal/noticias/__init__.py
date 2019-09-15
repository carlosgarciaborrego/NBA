from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
import sqlite3
import os.path
from django.utils.html import strip_tags
from lxml.doctestcompare import strip
from urllib.request import urlretrieve

if os.path.exists("html.txt"):
    print("HTML was extracted in the past")
else:   
    f = open("html.txt","a",encoding='utf-8')
    f1 = urlretrieve('https://es.nba.com/news','html1.txt')
    abrir1 = open("html1.txt","r",encoding='utf-8')
    f2 = urlretrieve('https://es.nba.com/all/news/page/2','html2.txt')
    abrir2 = open("html2.txt","r",encoding='utf-8')
    f3 = urlretrieve('https://es.nba.com/all/news/page/3','html3.txt')
    abrir3 = open("html3.txt","r",encoding='utf-8')
    f4 = urlretrieve('https://es.nba.com/all/news/page/4','html4.txt')
    abrir4 = open("html4.txt","r",encoding='utf-8')
    f5 = urlretrieve('https://es.nba.com/all/news/page/5','html5.txt')
    abrir5 = open("html5.txt","r",encoding='utf-8')
    f.write(str(abrir1.read()))
    f.write(str(abrir2.read()))
    f.write(str(abrir3.read()))
    f.write(str(abrir4.read()))
    f.write(str(abrir5.read()))
    f.close()
    abrir1.close()
    abrir2.close()
    abrir3.close()
    abrir4.close()
    abrir5.close()
    
f = open("html.txt","r",encoding='utf-8')    
s = BeautifulSoup(f,"html.parser")
f.close()
    
l = s.find_all("div",class_="card__headline")
j = s.find_all("a",class_="card__link")
h = s.find_all("span",class_="card__published-date")
e = s.find_all("a",class_=["card__label","card__label--link"])

conn = sqlite3.connect('as.db')
conn.text_factory = str
conn.execute("DROP TABLE IF EXISTS NOTICIAS") 
conn.execute('''CREATE TABLE NOTICIAS
    (TITULAR TEXT NOT NULL,
    FECHA    TEXT    NOT NULL,
    REFERENCIA   TEXT NOT NULL,
    URLPARTIDO   TEXT NOT NULL,
    URLEQUIPO    TEXT NOT NULL);''')

for i in range(len(l)):
    titular=strip_tags(l[i]).strip()
    fecha = strip_tags(h[i]).strip()
    ref = strip_tags(e[i]).strip()
    urlPartido = j[i].get("href")
    urlEquipo = e[i].get("href")
    
    conn.execute("""INSERT INTO NOTICIAS VALUES(?,?,?,?,?)""",(titular,fecha,ref,urlPartido,urlEquipo))
conn.commit()    
cursor = conn.execute("""SELECT * FROM NOTICIAS""")
  
for row in cursor:
    s = str(row[0])+'|'+str(row[1])+'|'+str(row[2])+'|'+str(row[3])+'|'+str(row[4])
    print(s)

conn.close()    