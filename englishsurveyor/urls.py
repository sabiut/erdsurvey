from django.urls import path
from . import views

urlpatterns = [
    path('takesurvey/<int:object_id>/', views.survey_view, name='takesurvey'),
    path('survey_fill/', views.survey_fill, name="fill-survey"),

]
