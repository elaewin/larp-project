from django.conf.urls import include, url
from events.views import event_edit, event_new, event_view, list_view, past_list_view, home_view, tag_view

urlpatterns = [
    url(r'^$', home_view, name="home_page"),
    url(r'^events/$', list_view, name="events_index"),
    url(r'^events/(?P<event_id>\d+)/$', event_view, name="event_detail"),
    url(r'^events/new/$', event_new, name='event_new'),
    url(r'^events/(?P<pk>\d+)/edit/$',  event_edit,  name='event_edit'),
    url(r'^events/past/$', past_list_view, name="events_past"),
    url(r'^events/tag/(?P<slug>[-\w]+)/$', tag_view, name="tagged"),
]
