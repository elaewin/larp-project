from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


from django.template import RequestContext, loader
from events.models import Event


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
    events = published.order_by('-published_date')
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
