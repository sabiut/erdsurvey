from django.urls import path
from . import views

urlpatterns = [

    path('english/', views.english, name='english'),
    path('french', views.french, name='french'),
    path('bislama/', views.bislama, name='bislama'),
    path('create_new_survey/', views.create_new_survey, name='create_new_survey'),
    path('add_question/<int:survey_id>/', views.add_question, name='add_question'),
    path('add_choice/<int:question_id>/', views.add_choice, name='add_choice'),
    path('add_textbox_choice/<int:question_id>/', views.add_textbox_choice, name='add_textbox_choice'),
    path('add_checkbox_choice/<int:question_id>/', views.add_checkbox_choice, name='add_checkbox_choice'),
    path('archived_survey/', views.archived_survey, name='archived_survey'),

]
