from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})

def about_view(request,*args,**kwargs):
    my_context = {
        "my_text":"this is about us",
        "my_number": 123,
        "my_list": [1313 , 4231 , 312 , "Abc"]
    }

    return render(request,"about.html",my_context)    