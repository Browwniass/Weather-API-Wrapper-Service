from django.urls import path, include
from weather.views import WeatherForecastView, WeatherForecastCurrentView


urlpatterns = [
    path('weather-forecast/', WeatherForecastView.as_view(), name='weather'),
    path('weather-forecast-current/', WeatherForecastCurrentView.as_view(), name='weather_current'),
]