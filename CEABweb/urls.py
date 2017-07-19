from django.conf.urls import include, url
from django.contrib import admin
from siad.views import atributos_meta, contactos
from promotoria.views import promotorianva, formulario_buscar, nuevo_prospecto, buscar_aspirante,detalleAspirante,editaProspecto
from controlescolar.views import buscar_alumnos, control_escolares, nuevo_alumno, formulario_buscar_alumno, consulta_adeudos
from contabilidad.views import contabilidad, nuevo_egreso, consulta_adeudo_alumnos


urlpatterns = [
    # Examples:
    # url(r'^$', 'CEABweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('siad.urls')),
	url(r'^formulario_buscar/$', formulario_buscar, name='formulario_buscar'),
    url(r'^formulario_buscar_alumno/$', formulario_buscar_alumno, name='formulario_buscar_alumno'),
	url(r'^buscar/$', buscar_aspirante),
    url(r'^buscar_alumnos/$', buscar_alumnos, name='buscar_alumnos'),
    url(r'^control_escolares/$', control_escolares, name='control_escolares'),
    url(r'^contabilidad/$', contabilidad, name='contabilidad'),
    url(r'^promotoria/$', promotorianva, name='promotorianva'),
    url(r'^nuevo_prospecto/$', nuevo_prospecto, name='nuevo_prospecto'),
    url(r'^nuevo_alumno/$', nuevo_alumno, name='nuevo_alumno'),
    url(r'^nuevo_egreso/$', nuevo_egreso, name='nuevo_egreso'),
    url(r'^(?P<id>\d+)/editaProspecto/$', editaProspecto, name='editaProspecto'),
    #url(r'^(?P<id>\d+)/$', aspirante, name='detail'),
    url(r'^(?P<id>\d+)/$', detalleAspirante, name='detalleAspirante'),
    url(r'^consulta_adeudos/(?P<min>\d+)/$', consulta_adeudos, name='colsulta_adeudos'),
    url(r'^consulta_adeudo_alumnos/$', consulta_adeudo_alumnos, name='adeudo_alumnos'),

]
