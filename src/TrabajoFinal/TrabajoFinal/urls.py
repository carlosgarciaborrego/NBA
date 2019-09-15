"""TrabajoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from principal import views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clasificacion/',views.lista_equipos),
    path('populate/', views.populateDB),
    path('',views.index),
    path('noticias/',views.lista_noticias),
    path('jornadas/',views.lista_jornadas),
    path('noticias/Atlanta',views.noticiasAtl),
    path('noticias/Boston',views.noticiasBos),
    path('noticias/Chicago',views.noticiasChi),
    path('noticias/Charlotte',views.noticiasChar),
    path('noticias/Brooklyn',views.noticiasBro),
    path('noticias/Cleveland',views.noticiasCle),
    path('noticias/Miami',views.noticiasMia),
    path('noticias/NewYork',views.noticiasNY),
    path('noticias/Detroit',views.noticiasDet),
    path('noticias/Orlando',views.noticiasOrl),
    path('noticias/Philadelphia',views.noticiasPhi),
    path('noticias/Indiana',views.noticiasInd),
    path('noticias/Washington',views.noticiasWas),
    path('noticias/Toronto',views.noticiasTor),
    path('noticias/Milwakee',views.noticiasMil),
    path('noticias/Dallas',views.noticiasDal),
    path('noticias/Denver',views.noticiasDen),
    path('noticias/GoldenState',views.noticiasGSW),
    path('noticias/Houston',views.noticiasHou),
    path('noticias/Minnesota',views.noticiasMin),
    path('noticias/Clippers',views.noticiasLAC),
    path('noticias/Memphis',views.noticiasMem),
    path('noticias/Oklahoma',views.noticiasOKL),
    path('noticias/Lakers',views.noticiasLAL),
    path('noticias/Pelicans',views.noticiasNOP),
    path('noticias/Portland',views.noticiasPor),
    path('noticias/Phoenix',views.noticiasPho),
    path('noticias/SanAntonio',views.noticiasSAS),
    path('noticias/Utah',views.noticiasUtah),
    path('noticias/Sacramento',views.noticiasSac),
    path('noticias/NBA',views.noticiasNBA),   
]
