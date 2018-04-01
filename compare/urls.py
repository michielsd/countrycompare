from django.conf.urls import url

from compare import views

urlpatterns = [
    url(r'^$', views.lookup, name='lookup'),
]