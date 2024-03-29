from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Event, Submission
from .forms import submissionForm
from django.contrib.auth.decorators import login_required
# Create your views here.
class IndexView(View):
    def get(self, request):
        
        try:
            limit = int(request.GET.get('limit'))
        except:
            limit = 4 
        print("-----------------------------")
        print(limit)
        
        users = get_user_model()
        Users = users.objects.filter(hackthon_participant=True)
        events = Event.objects.all()
        count = Users.count()

        paginator = Paginator(Users, limit)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        pages = list(range(1, (paginator.num_pages + 1)))

        context = {
            'users':Users,
            'events': events,
            'count': count,
            'user_list':Users[0:limit],
            'page_obj':page_obj,
            'paginator':paginator,
            'page_number':page_number,
            'pages':pages
        }
        return render(request, 'core/index.html', context)
    
    def post(self, request):
        return HttpResponse("this is a post request")
    
from datetime import datetime

class EventView(View):
    def get(self, request, pk):
        
        try:
            event = Event.objects.get(id=pk)
            user = request.user
            print("date: ", event.registration_deadline)
            deadline = event.registration_deadline.timestamp()
            now = datetime.now().timestamp()
            passed_deadline = (deadline < now )
            
            
            if(user.is_authenticated):
                
                submitted = Submission.objects.filter(participant = request.user, event=event).exists()
                print('submitted> > > :   ', submitted)
            else:
                submitted = False
        except Event.DoesNotExist:
            messages.warning(request, "event not found")
            return redirect(request.META.get("HTTP_REFERER", '/'))
            # return render(request, 'core/event.html', context)
        context = {
            'event':event,
            'submitted':submitted,
            'deadline_passed':passed_deadline
        }
        return render(request, 'core/event.html', context)
    

    def post(self, request, pk):
        
       
        event = Event.objects.get(pk=pk)
        user = request.user
        print('--------------------------------', event.participants.filter(email = user.email).exists())
        if event.participants.filter(email = user.email):
            messages.success(request, f"{user}, You are no longer a participant of {event}")
            event.participants.remove(user)
            return redirect ('event', event.id )
        
        context = {
            'event':event,
        }
        return render(request, 'core/event.html', context)
    
    
class Confirm_Event_Registration(LoginRequiredMixin, View):
    def get(self, request, pk):
        
        try:
            event = Event.objects.get(pk=pk)
            deadline = event.registration_deadline.timestamp()
            now = datetime.now().timestamp()
            passed_deadline = (deadline < now )
            if passed_deadline:
                messages.info(request, "event registration is already closed")
                return HttpResponseRedirect(reverse ('event', args=[str(event.pk)]))
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
    
@login_required(login_url='login')    
def project_submission(request, id):
    event = Event.objects.filter(id=id).first()
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
        elif form.errors:
            for err in list(form.errors.values()):
                messages.error(request, err)

    context = {'event':event,
               'form':form}
    return render(request, 'core/project_submission.html', context)

# @login_required()
def UpdateSubmission(request, id):
    try:
        submission = Submission.objects.get(id=id, participant = request.user)
    except:
        # return HttpResponse(f'<b><script> alert("You cant be here!!")</script>')
        messages.info(request, "You are not authorized for this operation :)")
        return redirect('/')
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