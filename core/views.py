from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'core/index.html')
    
    def post(self, request):
        return HttpResponse("this is a post request")
