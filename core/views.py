from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
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
            messages.warning(request, "event not found")
            return redirect(request.META.get("HTTP_REFERER", '/'))
            # return render(request, 'core/event.html', context)
        context = {
            'event':event
        }
        return render(request, 'core/event.html', context)

class Confirm_Event_Registration(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return HttpResponse("404, not found!")
        context = {
            'event':event
        }

        return render(request, 'core/event_confirmation.html', context)
    
    def post(self, request, pk):
        try:
            user = request.user
            event = Event.objects.get(pk=pk)

            #check if user is already a participant
            if user in event.participants.all():
                messages.info(request, 'You have been added already!')
                return redirect('event', event.pk)
            else:
                event.participants.add(request.user)
                messages.success(request, f'{request.user}, You have been added as a participant of this event')
                return redirect('event', event.pk)
        except Event.DoesNotExist:
            return HttpResponse("error, not found!")
        context = {
            'event':event
        }

        return render(request, 'core/event_confirmation.html', context)