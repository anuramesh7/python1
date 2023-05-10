from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieform

# Create your views here.
def index(request):
    Mov=movie.objects.all()
    context={'movielist':Mov


    }
    return  render(request,"index.html",context)

def detail(request,movie_id):
    movi=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movi})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        mo=movie(name=name,desc=desc,Year=year,img=img)
        mo.save()
        return render(request,'add.html')
    else:
        return render(request,'add.html')



def edit(request,id):
    mo=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=mo)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':mo})
def delete(request,id):
    if request.method=="POST":
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request, 'delete.html')


