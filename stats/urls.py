from django.urls import path
from rest_framework import routers
from . import views
 
urlpatterns = [
   path('', views.home, name = 'stats-home'),
   path('about/', views.about, name="stats-about"),
   path('fighters/', views.fighters, name="stats-fighters"),
   path('api/', views.api, name="stats-api")
]
