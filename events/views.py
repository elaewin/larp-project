import datetime
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
# from django.template import RequestContext, loader
from events.models import Event
from events.forms import EventForm, SignUpForm


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def home_view(request):
    """
    Default view. Redirects to the landing page for the site. 
    """
    return render(request, 'home.html', {})


def list_view(request):
    """
    View for events that have not taken place. 
    Excludes events not published in the admin view as well as any events with 
    a datetime stamp that evaluates before 'now' via the python datetime module.
    """
    published = Event.objects.exclude(published_date__exact=None).exclude(date__lt=datetime.datetime.now())
    events = published.order_by('date')
    context = {'events': events}
    return render(request, 'list.html', context)


def past_list_view(request):
    """
    View for events that have already taken place. 
    Excludes events not published in the admin view as well as any events with 
    a datetime stamp that evaluates after 'now' via the python datetime module.
    """
    published = Event.objects.exclude(published_date__exact=None)
    events = published.order_by('date').exclude(date__gt=datetime.datetime.now())
    context = {'events': events}
    return render(request, 'past_list.html', context)


@login_required
def tag_view(request, slug):
    published = Event.objects.exclude(published_date__exact=None)
    events = published.filter(tags__slug=slug).order_by('date')
    context = {'events': events}
    return render(request, 'tags_list.html', context)


@login_required
def event_view(request, event_id):
    """
    View for details of a specific event.
    """
    published = Event.objects.exclude(published_date__exact=None)
    try:
        event = published.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404
    context = {'event': event}
    return render(request, 'detail.html', context)


def sign_up_view(request, event_id):
    """
    View for details of a specific event.
    """
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.participating_in = event.player
            signup.save()
            return redirect('event_detail', event.pk)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def event_new(request):
    """
    View for creation of a new event.
    """
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.published_date = datetime.datetime.now()
            event.save()
            form.save_m2m()
            return redirect('event_detail', event.pk)
    else:
        form = EventForm()
    return render(request, 'event_edit.html', {'form': form})


@login_required
def event_edit(request, pk):
    """
    View for editing an existing event.
    """
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.published_date = datetime.datetime.now()
            event.save()
            form.save_m2m()
            return redirect('event_detail', event.pk)
    else: 
        form = EventForm(instance=event)
    return render(request, 'event_edit.html', {'form': form})


# @login_required
# def event_view(request, event_id):
#     """
#     View for details of a specific event.
#     """
#     current_date = datetime.datetime.now()
#     published = Event.objects.exclude(published_date__exact=None)
#     event = get_object_or_404(published, pk=event_id)
#     form = SignUpForm(request.POST, instance=event)
#     try:
#         event = published.get(pk=event_id)
#         if request.method == "POST":
#             form = SignUpForm(request.POST)
#             if form.is_valid():
#                 if current_date - form.age > 21:
#                     signup = form.save(commit=False)
#                     signup.participating_in = event.player
#                     signup.save()
#                     # form.save_m2m()
#                     return redirect('signup.html', event.pk)
#                 else:
#                     return redirect('signup_fail.html', event.pk)
#         else:
#             form = SignUpForm()
#     except Event.DoesNotExist:
#         raise Http404
#     context = {'event': event, 'form': form}
#     return render(request, 'detail.html', context)


# if ContactForm.is_valid():
#     subject = ContactForm.cleaned_data['subject']
#     message = ContactForm.cleaned_data['message']
#     sender = ContactForm.cleaned_data['sender']
#     cc_myself = ContactForm.cleaned_data['cc_myself']

#     recipients = [Event.contact_email]
#     if cc_myself:
#         recipients.append(sender)

#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')
