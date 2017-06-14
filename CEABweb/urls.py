from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from siad.views import atributos_meta
from siad import views
from promotoria import views
from controlescolar import views
from contabilidad import views

=======
from siad.views import atributos_meta, contactos
from promotoria.views import promotorianva, formulario_buscar, nuevo_prospecto, buscar_aspirante
from controlescolar.views import buscar_alumnos, control_escolares, nuevo_alumno, formulario_buscar_alumno
from contabilidad.views import contabilidad, nuevo_egreso
>>>>>>> guardar
urlpatterns = [
    # Examples:
    # url(r'^$', 'CEABweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('siad.urls')),
    url(r'^meta/', atributos_meta),
	url(r'^formulario_buscar/$', formulario_buscar, name='formulario_buscar'),
    url(r'^formulario_buscar_alumno/$', formulario_buscar_alumno, name='formulario_buscar_alumno'),
	url(r'^buscar/$', buscar_aspirante),
    url(r'^buscar_alumnos/$', buscar_alumnos, name='buscar_alumnos'),
	url(r'^contactos/$', contactos),
    url(r'^control_escolares/$', control_escolares, name='control_escolares'),
    url(r'^contabilidad/$', contabilidad, name='contabilidad'),
    url(r'^promotoria/$', promotorianva, name='promotorianva'),
    url(r'^nuevo_prospecto/$', nuevo_prospecto, name='nuevo_prospecto'),
    url(r'^nuevo_alumno/$', nuevo_alumno, name='nuevo_alumno'),
    url(r'^nuevo_egreso/$', nuevo_egreso, name='nuevo_egreso'),
]
