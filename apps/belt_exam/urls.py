from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^result$', views.result),
    url(r'^login$', views.login),
    url(r'^add$', views.add),
    url(r'^items$', views.items),
]
