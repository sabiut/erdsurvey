from django.urls import path
from . import views

urlpatterns = [

    path('signin/', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard'),

]
