from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import User
from core.models import Event

# Create your views here.
def loginPage(request):
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