from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.hashers import make_password
from .models import User
from core.models import Event
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import SignupForm, EditAccountForm
# Create your views here.
def signUpPage(request):
    # user = User.objects
    form  = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

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

            # for redirecting to previous page
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:

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


class Account(LoginRequiredMixin,View):
    def get(self, request):
        context = {}
        
        return render(request, 'users/account.html', context)
    def post(self, request):
        pass


class EditAccount(LoginRequiredMixin, View):
    def get(self, request):
        form = EditAccountForm(instance=request.user)
        context = {'form':form}
        
        return render(request, 'users/user-form.html', context)
    def post(self, request):
        form = EditAccountForm(request.POST, request.FILES,instance = request.user)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            messages.success(request, "changes saved")
            return redirect('account')
        
        return render(request, 'users/user-form.html', context)
    

class ChangePassword(LoginRequiredMixin,View):
    def get(self, request, id):
       

        return render(request, "users/change-password.html")
    
    def post(self, request, id):
       password1 = request.POST['password1']
       password2 = request.POST['password2']

       user = request.user

       if password1 == password2:
           if len(password1) < 8:
               messages.error(request, "length of password must be upto 8", {'data':request.POST})
               return render(request, "users/change-password.html")
           password = make_password(password1)
           user.password = password
           user.save()
           messages.success(request, "password changed successfully!")
           return redirect("account")

       messages.error(request, "password does not match")
       return render(request, "users/change-password.html", {'data':request.POST})