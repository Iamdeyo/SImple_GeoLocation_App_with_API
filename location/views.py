from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def test(req):
#     return HttpResponse("Hello Moto")

def index(request):
    return render(request, 'location/index.html', {})