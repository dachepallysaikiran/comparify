from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
def index(request):
    return render(request,'home.html') 
# def results(request):
#     keys=request.GET.get('key','nothing')
#     param={'key':keys}
#     print('hiii')
#     return render(request,'results.html',param) 
def results2(request):
    products= Product.objects.all()
    keys=request.GET.get('key','nothing')
    k=[]
    for i in products: 
        if i.category==keys:
            k.append(i)
    n= len(k)
    if (n==0):
        return render(request,'noresults.html')

    range1=range(n)
    param={'key1':keys,'range':range1,'product':k} 
    return render(request,'results2.html',param)