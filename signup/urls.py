from django.urls import path
from . import views

urlpatterns = [

    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('archive/<int:archive_id>/', views.archive_survey, name='archive'),
    path('edit_survey/<int:get_survey_id>/', views.edit_survey, name='edit_survey'),
    path('delete_survey/<int:get_survey_id>/', views.delete_survey, name='delete_survey'),

]
