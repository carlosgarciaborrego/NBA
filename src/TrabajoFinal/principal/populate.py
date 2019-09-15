from __future__ import division
from principal.models import Equipo,Noticia,Jornada


def deleteTables():
    Equipo.objects.all().delete()
    Noticia.objects.all().delete()
    Jornada.objects.all().delete()

def populateClasificacion():
    print("Cargando tabla")
    
    fileobj = open("clasificacion/clasificacion.txt","r")
    line = fileobj.readline()
    while line:
        data = line.split('|')
        if len(data)>1:
            nomb = data[0]
            vict = data[1]
            derr = data[2]
            porc = data[3]
            dife = data[4]
            ptof = data[5]
            ptoc = data[6]

            Equipo.objects.create(nombre=nomb, victorias=vict, derrotas=derr, porcentaje=porc, diferencia=dife, puntosFavor=ptof, puntosContra=ptoc)
        line = fileobj.readline()      
    fileobj.close()            
                
    print("Equipos insertedos: " + str(Equipo.objects.count()))       
    
def populateNoticias():
    print("Cargando noticias")
    
    fileobj = open("noticias/noticias.txt","r")    
    line = fileobj.readline()
    while line:
        data = line.split('|')
        if len(data)>1:
            tit = data[0]
            fec = data[1]
            ref = data[2]
            urlP = data[3]
            urlE = data[4]
    
            Noticia.objects.create(titular=tit, fecha=fec, referencia=ref, urlPartido=urlP, urlEquipo=urlE)
        line = fileobj.readline()
    fileobj.close()        
            
    print("Noticias insertedas: " + str(Noticia.objects.count()))           
            
def populateJornada():
    print("Cargando jornadas")
    
    fileobj = open("jornadas/jornadas.txt","r")    
    line = fileobj.readline()
    while line:
        data = line.split('|')
        if len(data)>1:
            num = data[0]
            eloc = data[1]
            evis = data[2]
            ptoL = data[3]
            ptoV = data[4]
            ho = data[5]
    
            Jornada.objects.create(numero=num, local=eloc, visitante=evis, puntosL=ptoL, puntosV=ptoV, hora = ho)
        line = fileobj.readline()
    fileobj.close()        
            
    print("Jorndas insertedas: " + str(Jornada.objects.count()))           
                                 
            
            
def populateDatabase():
    deleteTables()
    populateClasificacion()
    populateNoticias()
    populateJornada()

if __name__ == '__main__':
    populateDatabase()