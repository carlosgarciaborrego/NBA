from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
import sqlite3
import os.path 
 
f = urllib.request.urlopen("https://resultados.as.com/resultados/baloncesto/nba/calendario/")
s = BeautifulSoup(f,"lxml")
    
l = s.find_all("div", class_= ["cont-modulo","resultados"])

conn = sqlite3.connect('as.db')
conn.text_factory = str 
conn.execute("DROP TABLE IF EXISTS JORNADAS") 
conn.execute('''CREATE TABLE JORNADAS
    (NUMERO INT NOT NULL,
    LOCAL    TEXT    NOT NULL,
    VISITANTE       TEXT NOT NULL,
    PTOLOCAL         TEXT,
    PTOVISITANTE      TEXT,
    HORA     TEXT);''')


for i in l:
    jornada = int(re.compile('\d+').search(i['id']).group(0))
    partidos = i.find_all("tr",id)
    for p in partidos:
        equipos= p.find_all("span")
        resultados = p.find("span",class_=["resultado"])
        for z in equipos:
            if (z.get('content')):
                nba = z.get('content')
                trocitos = nba.split()
                if(str(trocitos[3])=="-"):
                    local = str(trocitos[1])+" "+str(trocitos[2])
                    visitante = ""
                    for t in trocitos[4:]:
                        visitante = visitante +str(t)  
                else:
                    local = str(trocitos[1])+" "+str(trocitos[2])+" "+str(trocitos[3])
                    visitante = ""
                    for t in trocitos[5:]:
                        visitante = visitante+t
                anotacion=re.compile('(\d+).*(\d+)').search(resultados.string.strip())      
                encuentro = anotacion[0]
                
                if str(encuentro).__contains__(":"):
                    ptoL=""
                    ptoV=""
                    conn.execute("""INSERT INTO JORNADAS VALUES(?,?,?,?,?,?)""",(jornada,local,visitante,ptoL,ptoV,encuentro))
                else:
                    ptoL=encuentro.split()[0]
                    ptoV=encuentro.split()[2]
                    encuentro = ""
                    conn.execute("""INSERT INTO JORNADAS VALUES(?,?,?,?,?,?)""",(jornada,local,visitante,ptoL,ptoV,encuentro))
 
conn.commit()

cursor = conn.execute("""SELECT * FROM JORNADAS ORDER BY NUMERO""")
#calendario por equipo
#cursor = conn.execute("""SELECT * FROM JORNADAS WHERE (LOCAL LIKE 'Milwaukee Bucks' OR VISITANTE LIKE ' Milwaukee Bucks') ORDER BY NUMERO""")
#elegir jornada
#cursor = conn.execute("""SELECT * FROM JORNADAS""")

if os.path.exists("jornadas.txt"):
    print("HTML was extracted in the past")
else: 
    archivo = open("jornadas.txt","a",encoding='utf-8')

    for row in cursor:
        s = str(row[0])+'|'+str(row[1])+'|'+str(row[2])+'|'+str(row[3])+'|'+str(row[4])+'|'+str(row[5]) + "\n"
        print(s)
        archivo.write(str(s))
    archivo.close() 
conn.close()    