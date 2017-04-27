from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^editar_prospecto/$', views.editar_prospecto, name='editar_prospecto'),
	]
