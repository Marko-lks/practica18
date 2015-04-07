from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalle/(?P<question_id>[0-9]+)/$', views.modificar, name='modificar'),
    url(r'^nuevo/$', views.nuevo, name='nuevo'),
    url(r'^eliminar/(?P<question_id>[0-9]+)/$', views.eliminar, name='eliminar'),
]