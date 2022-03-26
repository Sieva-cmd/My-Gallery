from email import message
from django.http import Http404
from django.shortcuts import render
from .models import Image,Location,Category
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def index(request):
    location =Location.objects.all()
    photos =Image.filter_by_location(location)
    return render(request,'index.html',{"photos":photos})
    

def search_results(request):
    # print(dir(request))
    if 'photo' in request.GET and request.GET["photo"]:
        search_item =request.GET.get("photo")
        searched_images =Image.search_image_by_category(search_item)
        message =f"{search_item}"

        return render(request,'search.html',{"message":message,"photos":searched_images})
    else:
        message ="You have not searched any Image"
        return render(request,'search.html',{"message":message})    

def get_image_by_id(request,image_id):
    try: 
        photo =Image.objects.get(id=image_id)

    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'image.html',{"photo":photo} )    

