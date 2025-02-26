from django.urls import path
from home import views

urlpatterns = [
    path('', views.aqi_pollutants, name='aqi_pollutants'),
    path("aqi_results", views.aqi_results, name='aqi_results')
]