from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
import os
from demoapp.forms import LogForm
'''def cutu(request): 
   path=request.path
   response="Adreka<333"
   return HttpResponse(response)

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 
# Create your views here.
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request): 
    return render(request, "form.html") 

def submitform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    f=open('data.txt','a+')
    f.write(f"Name:{name} UserID:{id}")
    f.close()
    return HttpResponse("Name:{} UserID:{}".format(name, id)) '''


def form_view(request):
    form=LogForm() 
    if request.method== 'POST':
        form=LogForm(request.POST)
        if form.is_valid():
         form.save()
    context={"form":form}
    return render(request,"home.html",context)
