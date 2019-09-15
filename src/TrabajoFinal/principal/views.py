from django.shortcuts import render
from principal.models import Equipo, Noticia, Jornada
from principal.populate import populateDatabase
# Create your views here.

def index(request): 
    return render(request,'index.html')

def populateDB(request):
    populateDatabase()
    return render(request,'populate.html')

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request,'lista_equipos.html',{'equipo':equipos})

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'lista_noticias.html',{'noticias':noticias})

def lista_jornadas(request):
    jornadas = Jornada.objects.all()
    return render(request,'lista_jornadas.html',{'jornadas':jornadas})

def noticiasAtl(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasAtlanta.html',{'noticias':noticias})

def noticiasBos(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasBoston.html',{'noticias':noticias})

def noticiasChi(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasChicago.html',{'noticias':noticias})

def noticiasChar(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasCharlotte.html',{'noticias':noticias})

def noticiasBro(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasBrooklyn.html',{'noticias':noticias})

def noticiasCle(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasCleveland.html',{'noticias':noticias})

def noticiasMia(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasMiami.html',{'noticias':noticias})

def noticiasNY(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasNewYork.html',{'noticias':noticias})

def noticiasDet(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasDetroit.html',{'noticias':noticias})

def noticiasOrl(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasOrlando.html',{'noticias':noticias})

def noticiasPhi(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasPhiladelphia.html',{'noticias':noticias})

def noticiasInd(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasIndiana.html',{'noticias':noticias})

def noticiasWas(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasWashington.html',{'noticias':noticias})

def noticiasTor(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasToronto.html',{'noticias':noticias})

def noticiasMil(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasMilwakee.html',{'noticias':noticias})

def noticiasDal(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasDallas.html',{'noticias':noticias})

def noticiasDen(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasDenver.html',{'noticias':noticias})

def noticiasGSW(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasGoldenState.html',{'noticias':noticias})

def noticiasHou(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasHouston.html',{'noticias':noticias})

def noticiasMin(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasMinnesota.html',{'noticias':noticias})

def noticiasLAC(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasClippers.html',{'noticias':noticias})

def noticiasMem(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasMemphis.html',{'noticias':noticias})

def noticiasOKL(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasOklahoma.html',{'noticias':noticias})

def noticiasLAL(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasLakers.html',{'noticias':noticias})

def noticiasNOP(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasPelicans.html',{'noticias':noticias})

def noticiasPor(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasPortland.html',{'noticias':noticias})

def noticiasPho(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasPhoenix.html',{'noticias':noticias})

def noticiasSAS(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasSanAntonio.html',{'noticias':noticias})

def noticiasUtah(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasUtah.html',{'noticias':noticias})

def noticiasSac(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasSacramento.html',{'noticias':noticias})

def noticiasNBA(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiasNBA.html',{'noticias':noticias})
