from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the homepage")
    # Create your views here.
def about(request):
    return render(request,'ABOUT.html')
def contact(request):
    return HttpResponse("contact number doesnot Exist")
def thanks(request):
    return render(request,'thanks.html')