from django.conf.urls import url
from events.views import stub_view

urlpatterns = [
    url(r'^$',
        stub_view,
        name="games_index"),
    url(r'^events/(?P<game_id>\d+)/$',
        stub_view,
        name="game_detail"),
]