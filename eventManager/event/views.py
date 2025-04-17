from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EventForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CommentForm

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registered_count = Registration.objects.filter(event=event).count()
    max_participants = event.max_participants
    is_registered = Registration.objects.filter(event=event, user=request.user).exists()

    from .forms import CommentForm
    comments = event.comments.all().order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect('event_detail', event_id=event.id)
    else:
        comment_form = CommentForm()

    return render(request, 'events/event_detail.html', {
        'event': event,
        'registered_count': registered_count,
        'max_participants': max_participants,
        'is_registered': is_registered,
        'comments': comments,
        'comment_form': comment_form,
    })



@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user  
            event.save()
            
            Registration.objects.create(event=event, user=request.user)
            
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if Registration.objects.filter(event=event, user=request.user).exists():
        return redirect('event_detail', event_id=event.id)

    registered_count = Registration.objects.filter(event=event).count()
    if event.max_participants and registered_count >= event.max_participants:
        return render(request, 'events/event_detail.html', {
            'event': event,
            'registered_count': registered_count,
            'max_participants': event.max_participants,
            'error_message': "Sorry, this event is fully booked."
        })

    if request.method == 'POST':
        Registration.objects.create(event=event, user=request.user)
        return redirect('event_detail', event_id=event.id)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('event_list')  
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

