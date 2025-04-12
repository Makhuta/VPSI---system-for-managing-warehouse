from django.conf.urls.i18n import set_language
from django.contrib.auth import views as auth_views
from django.urls import path


from . import views

urlpatterns = [
    path('lang/', set_language, name='set_language'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('settings/', views.page_settings, name='settings'),
    path('items/', views.items, name='items'),
    path("orders/", views.orders, name="orders"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path('add_item/', views.new_item, name='new_item'),
    path('add_order/', views.new_order, name='new_order'),
    path('add_supplier/', views.new_supplier, name='new_supplier'),
]