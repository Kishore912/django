from django.shortcuts import render
from .models import product
from .forms import ProductForm
# Create your views here.

def product_detail_view(request):
    obj = product.objects.get(id=1)
    context = {
        'title':obj.title,
        'description':obj.description,
        'price':obj.price
    }
    return render(request,"product/detail.html",context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        context={
        'form':form
        }    
    return render(request , "product/product_create.html",context)