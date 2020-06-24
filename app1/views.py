from django.shortcuts import render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.

def getdata(url):
    data = requests.get(url)
    return data.text

def get_json():
    file_path = staticfiles_storage.path('coordinates.json')
    with open(file_path,'r') as f:
        data = json.load(f)

    html_doc = getdata("https://www.mygov.in/covid-19")
    soup = BeautifulSoup(html_doc, 'html.parser')
    k = soup.tbody.get_text()
    k = (("\n"+k).split("\n\n"))[1:-1]

    datarow = {}
    for index,item in enumerate(k):
        value = item.split("\n")
        datarow[value[1].lower()] = {
            'coordinates':list(data.values())[index],
            'confirmed':value[2],
            'active':value[3],
            'recovered':value[4],
            'deceased':value[5]
        }
    return datarow

@api_view(['GET'])
def get_map_josn(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = get_json()
        print('Responsed')
        return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def coordinates(request):
    url = 'https://raw.githubusercontent.com/namantam1/indian_coordinated/master/india.json'
    resp = requests.get(url)
    data = json.loads(resp.text)
    return Response(data,status=status.HTTP_200_OK)

# Create your views here.
def home(request):
    return render(request,'app1/index.html')
