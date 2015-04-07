from django.conf.urls import include, url
from django.contrib import admin
from apps.inicio import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'practica18.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.inicio, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/', include('apps.inicio.urls')),
]
