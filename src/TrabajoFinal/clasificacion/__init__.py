from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
import sqlite3
from django.utils.html import strip_tags
import os.path

 
f = urllib.request.urlopen("https://www.hispanosnba.com/clasificacion-nba")
s = BeautifulSoup(f,"lxml")

l = s.find_all("table", class_= ["tblcla","responsive"], limit=2)

conn = sqlite3.connect('as.db')
conn.text_factory = str  
conn.execute("DROP TABLE IF EXISTS EQUIPOS") 
conn.execute('''CREATE TABLE EQUIPOS
    (NOMBRE    TEXT    NOT NULL,
    VICTORIAS       TEXT NOT NULL,
    DERROTAS          TEXT    NOT NULL,
    PORCENTAJE      TEXT    NOT NULL,
    DIFERENCIA      TEXT    NOT NULL,
    PF      TEXT    NOT NULL,
    PC      TEXT    NOT NULL);''')

for i in l:
    enlace = i.find_all("a")
    nom=[]
    for j in enlace:
        nom.append(j.get("title"))
        
    datos = i.find_all("td")
    lista=[]
    for z in datos:     
        d=strip_tags(z)
        lista.append(d)
        
    buena = [lista[x:x+11] for x in range(0,len(lista),11)]

    for x in range(15):
        nombre = nom[x]
        for y in range(1):
            victorias = buena[x][0]
            derrotas = buena[x][1]
            porcentaje = buena[x][2]
            diferencia = buena[x][3]
            pf = buena[x][4]
            pc = buena[x][5]
            conf = buena[x][6]
            div = buena[x][7]
            casa = buena[x][8]
            fuera = buena[x][9]
            u10 = buena[x][10]
    
    
            conn.execute("""INSERT INTO EQUIPOS VALUES(?,?,?,?,?,?,?)""",(nombre,victorias,derrotas,porcentaje,diferencia,pf,pc))
conn.commit()

cursor = conn.execute("""SELECT * FROM EQUIPOS ORDER BY PORCENTAJE DESC""")

if os.path.exists("clasificacion.txt"):
    print("HTML was extracted in the past")
else: 
    archivo = open("clasificacion.txt","a",encoding='utf-8')
    
    for row in cursor:
        s = str(row[0]) +'|'+ str(row[1]) +'|'+ str(row[2]) +'|'+ str(row[3])+'|'+ str(row[4])+'|'+ str(row[5])+'|'+ str(row[6]+"\n")   
        print(s)
        archivo.write(str(s))
    
    archivo.close()    
conn.close()