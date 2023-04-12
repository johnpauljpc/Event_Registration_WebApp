from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import User

# Create your views here.
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
        
        return render(request, 'users/account.html')
    def post(self, request):
        print(request.user)