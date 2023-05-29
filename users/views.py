from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import User
from core.models import Event
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
# Create your views here.
def signUpPage(request):
    # user = User.objects
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
        # user = User.
            user = form.save(commit=False)
            user.save()
            login(request, user)
            print("***********************************")
            print(user.name)
        
            print("***********************************")
            messages.success(request, f"Successfully registered!, Welcome {user.name}!")
            return redirect('account')
        elif form.errors:
            for err in list(form.errors.values()):
                messages.error(request, err)

        
        
    
    form  = SignupForm()
    context = {
        'page':"register",
        'form': form
    }
    return render(request, "users/login_register.html", context)

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

def logoutView(request):
    logout(request)
    messages.info(request, "You have logged out!")
    return redirect("index")


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