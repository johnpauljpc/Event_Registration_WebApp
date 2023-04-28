from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import User
from core.models import Event
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def loginPage(request):
    
    if request.method == 'POST':
        user = authenticate(email = request.POST['email'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome <b>{user}</b>!")
            return redirect('index')
        messages.error(request, "credentials provided is wrong!")
    context = {
        'page':"login"
    }    
    return render(request, "users/login_register.html", context)

def signUpPage(request):
    context = {
        'page':"register"
    }
    return render(request, "users/login_register.html", context)

class User_Profile(View):
    def get(self, request, pk):
        user = User.objects.filter(id = pk).first()

        context = {
            'user':user
        }
        return render(request, 'users/user_profile.html', context)


class Account(View):
    def get(self, request):
        context = {}
        
        return render(request, 'users/account.html', context)
    def post(self, request):
        print(request.user)