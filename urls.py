from django.urls import path
from . import views

app_name = "homeworkapp"
urlpatterns = [
    path("", views.index, name="index") ,
    path("add", views.add, name="add") ,
 
]