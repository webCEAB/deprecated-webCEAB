from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^prospecto_raiz/$', views.prospecto_raiz, name='prospecto_raiz'),
	]
