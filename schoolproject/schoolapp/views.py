from django.shortcuts import render, redirect
from .models import login
from .models import register
# Create your views here.
def home(request):

    return render(request,'home.html')

def log(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        pass_word = request.POST.get('pass_word')
        confirm_pass = request.POST.get('confirm_password')
        if pass_word == confirm_pass:
           reg = register(user_name=user_name,pass_word=pass_word,confirm_pass=confirm_pass)
           reg.save()
           return render(request,'login.html')

        return redirect('/register')
    return render(request, 'login.html')



def form(request):
     if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        log=login(username=username,password=password)
        log.save()
     return render(request,'form.html')



def reg(request):


    return render(request,'register.html')

def result(request):
    return render(request,'result.html')