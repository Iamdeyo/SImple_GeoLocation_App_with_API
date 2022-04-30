from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.
# def test(req):
#     return HttpResponse("Hello Moto")

def index(request):

    

    # to get receive data from the API
    geoLoc = requests.get("http://ip-api.com/json/24.48.0.1")

    # to convert the file from JSON to py dictionary  
    geoLoc_data_text = geoLoc.text
    geoLoc_data = json.loads(geoLoc_data_text)


    return render(request, 'location/index.html', {'data': geoLoc_data})