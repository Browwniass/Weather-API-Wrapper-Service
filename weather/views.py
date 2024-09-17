from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from config.settings import env

class WeatherForecastView(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'Moscow')
        api_key = env.str('API_KEY', 'your_api_key')

        date_range = request.query_params.get('date_range', '')
        
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}{date_range}?unitGroup=metric&elements=datetime%2Ctempmax%2Ctempmin%2Ctemp%2Ccloudcover%2Cdescription&include=days%2Calerts&key={api_key}&contentType=json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class WeatherForecastCurrentView(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'Moscow')
        api_key = 'PGR6PSK8827RP7QK7HA38JQLS'

        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/today?unitGroup=metric&elements=datetime%2Ctempmax%2Ctempmin%2Ctemp%2Cdescription&include=current%2Cevents%2Chours&key={api_key}&contentType=json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
