from django.conf.urls import include, url
from django.contrib import admin
from siad.views import atributos_meta
urlpatterns = [
    # Examples:
    # url(r'^$', 'CEABweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('siad.urls')),
    url(r'^meta/',atributos_meta, name='atributos_meta'),
]
