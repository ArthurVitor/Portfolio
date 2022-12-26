from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('detailed_project:<int:id>', views.detailed_project, name='detailed_project'),
]