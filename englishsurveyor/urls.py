from django.urls import path
from . import views

urlpatterns = [
    path('takesurvey/<int:object_id>/', views.survey_view, name='takesurvey')

]
