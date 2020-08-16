from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=F8D7FC56-2B41-4B5E-8110-3B4639ABAC30')
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
       api = 'Error ...'
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})