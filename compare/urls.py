from django.conf.urls import url
from django.views.generic import TemplateView

from compare import views

urlpatterns = [
    url(r'^', views.lookup, name='lookup'),
]