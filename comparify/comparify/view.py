# i jhave creaed the file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    print('hjgjh')
    return render(request,'home.html') 
# def results(request):
#     keys=request.GET.get('key','nothing')
    
#     param={'key1':keys}
#     return render(request,'results.html',param) 
# def results2(request):
#     keys=request.GET.get('key','nothing')
#     param={'key1':keys}
#     return render(request,'results2.html',param) 
 