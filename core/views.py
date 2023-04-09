from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Event

# Create your views here.
class IndexView(View):
    def get(self, request):
        users = get_user_model()
        Users = users.objects.filter(hackthon_participant=True)
        events = Event.objects.all()
        context = {
            'users':Users,
            'events': events
        }
        return render(request, 'core/index.html', context)
    
    def post(self, request):
        return HttpResponse("this is a post request")
    

class EventView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return HttpResponse("event not found")
        context = {
            'event':event
        }
        return render(request, 'core/event.html', context)
