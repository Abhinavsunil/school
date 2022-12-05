from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def form(request):
    return render(request,'form.html')

def register(request):
    return render(request,'register.html')

def result(request):
    return render(request,'result.html')