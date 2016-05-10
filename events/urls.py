from django.conf.urls import url
from events.views import stub_view, list_view, event_view

urlpatterns = [
    url(r'^$',
        list_view,
        name="events_index"),
    url(r'^events/(?P<event_id>\d+)/$',
        event_view,
        name="event_detail"),
]