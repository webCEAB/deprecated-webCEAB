from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.index),
<<<<<<< HEAD
	url(r'^residencial/(?P<consumo>\d+)/$', views.residencial),
=======
>>>>>>> 30887fc7ea35921d60a63c31f12ef3fd60b2f469
	]
	
