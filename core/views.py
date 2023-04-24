from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Event, Submission
from .forms import submissionForm
from django.contrib.auth.decorators import login_required
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
            user = request.user
            submitted = Submission.objects.filter(participant = request.user, event=event).exists()
            print('submitted>>>>>>>>>>>>>>:', submitted)
            
        except Event.DoesNotExist:
            messages.warning(request, "event not found")
            return redirect(request.META.get("HTTP_REFERER", '/'))
            # return render(request, 'core/event.html', context)
        context = {
            'event':event,
            'submitted':submitted
        }
        return render(request, 'core/event.html', context)
    

    def post(self, request, pk):
        
       
        event = Event.objects.get(pk=pk)
        user = request.user
        if event.participants.filter(email = user.email).exists():
            messages.success(request, f"{user}, You are no longer a participant of {event}")
            event.participants.remove(user)
        
        context = {
            'event':event,
        }
        return render(request, 'core/event.html', context)
    
    
class Confirm_Event_Registration(LoginRequiredMixin, View):
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
    
@login_required()    
def project_submission(request, pk):
    event = Event.objects.filter(id=pk).first()
    form = submissionForm(initial={'participant':request.user, 'event':event})
    if request.user not in event.participants.all():
        messages.info(request, "you didn't register for the event, so You can't submit any project")
        return redirect('event', event.id)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if request.method == 'POST':
        
        form =submissionForm(request.POST)
        form.instance.event = event
        form.instance.participant = request.user
        if form.is_valid():
            form.save()
            return redirect('event', event.id)

    context = {'event':event,
               'form':form}
    return render(request, 'core/project_submission.html', context)

@login_required()
def UpdateSubmission(request, pk):
    submission = Submission.objects.get(id=pk, participant = request.user)
    event = submission.event
    form = submissionForm(instance=submission)
    context = {
        'event':event,
        'form':form

    }

    if request.method=='POST':
        form = submissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            messages.info(request, "submission updated successfully!")
            return redirect('account')
        for error in list(form.errors.values()):
            messages.error(request, error)
   
    return render(request, 'core/update-project-submission.html', context)