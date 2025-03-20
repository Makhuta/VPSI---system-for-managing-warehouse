from django.conf.urls.i18n import set_language
from django.urls import path


from . import views

urlpatterns = [
    path('lang/', set_language, name='set_language'),
    path('', views.index, name='index'),
]