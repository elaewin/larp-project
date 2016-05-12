import datetime
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
# from django.template import RequestContext, loader
from events.models import Event
from events.forms import ContactForm, EventForm


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    published = Event.objects.exclude(published_date__exact=None)
    events = published.order_by('date')
    context = {'events': events}
    return render(request, 'list.html', context)


def event_view(request, event_id):
    published = Event.objects.exclude(published_date__exact=None)
    try:
        event = published.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404
    context = {'event': event}
    return render(request, 'detail.html', context)


def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.published_date = datetime.datetime.now()
            event.save()
            return redirect('event_detail', event.pk)
    else:
        form = EventForm()
    return render(request, 'event_edit.html', {'form': form})


def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.published_date = datetime.datetime.now()
            event.save()
            return redirect('event_detail', event.pk)
    else: 
        form = EventForm(instance=event)
    return render(request, 'event_edit.html', {'form': form})



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
