from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Create your views here.
class IndexView(View):
    def get(self, request):
        users = get_user_model()
        Users = users.objects.all()
        context = {
            'users':Users
        }
        return render(request, 'core/index.html', context)
    
    def post(self, request):
        return HttpResponse("this is a post request")
