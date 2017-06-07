from django.conf.urls import include, url
from django.contrib import admin
from siad.views import atributos_meta
from siad import views
from promotoria.views import promotorianva
urlpatterns = [
    # Examples:
    # url(r'^$', 'CEABweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('siad.urls')),
    url(r'^meta/',atributos_meta),
	url(r'^formulario_buscar/$', views.formulario_buscar, name='formulario_buscar'),
    url(r'^formulario_buscar_alumno/$', views.formulario_buscar_alumno, name='formulario_buscar_alumno'),
	url(r'^buscar/$', views.buscar),
    url(r'^buscar_alumno/$', views.buscar_alumno),
	url(r'^contactos/$', views.contactos),
    url(r'^control_escolar/$', views.control_escolar, name='control_escolar'),
    url(r'^contabilidad/$', views.contabilidad, name='contabilidad'),
    url(r'^promotoria/$', promotorianva, name='promotorianva'),
    url(r'^nuevo_prospecto/$', views.nuevo_prospecto, name='nuevo_prospecto'),
]
