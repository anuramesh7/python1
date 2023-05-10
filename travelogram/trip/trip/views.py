from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Team
# Create your views here.
def demo (request):
    obj=Place.objects.all()
    obje=Team.objects.all()
    return render (request,'index.html',{'result':obj,'res':obje})
#def operations(request):
#    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
  ## r2=x-y
    #r3=x*y
    #r4=x/y
    #return render(request,'result.html',{'result':res,'result2':r2,'result3':r3,'result4':r4})

