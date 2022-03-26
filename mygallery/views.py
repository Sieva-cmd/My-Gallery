from django.shortcuts import render
from .models import Image,Location

def index(request):
    location =Location.objects.all()
    photos =Image.filter_by_location(location)


    return render(request,'index.html',{"photos":photos})

# Create your views here.
