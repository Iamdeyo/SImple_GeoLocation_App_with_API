from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.
# def test(req):
#     return HttpResponse("Hello Moto")

def index(request):

    # to receive user ip data from the API
    getUserIp = requests.get("https://api.ipify.org?format=json")
    # to convert the file from JSON to py dictionary 
    getUserIp_data = json.loads(getUserIp.text)
    # access the ip in dictionary
    Ip_data = getUserIp_data['ip']



    # to receive data from the API
    geoLoc = requests.get("http://ip-api.com/json/" + Ip_data)
    # to convert the file from JSON to py dictionary  
    geoLoc_data_text = geoLoc.text
    geoLoc_data = json.loads(geoLoc_data_text)


    return render(request, 'location/index.html', {'data': geoLoc_data,})