from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	#url(r'^$', views.instrucciones),
	#url(r'^residencial/(?P<consumo>\d+)/$', views.residencial),
	#url(r'^comercial/(?P<consumo>\d+)/$', views.comercial),
	#url(r'^documentacionIncompleta/$', views.docIncompleta),
	]
	
