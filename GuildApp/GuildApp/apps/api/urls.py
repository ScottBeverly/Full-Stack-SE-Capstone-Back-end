from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.api.views import RoleDetailsView, RoleListCreateView
from apps.api.views import ClassDetailsView, CreateClassView
from apps.api.views import BossDetailsView, CreateBossView
from apps.api.views import DifficultyDetailsView, DifficultyListCreateView
from apps.api.views import PlayerDetailsView, CreatePlayerView


urlpatterns = {
    url(r'^role-list/$', RoleListCreateView.as_view(), name='Role-list'),
    url(r'^role-update/(?P<pk>[0-9]+)/$', RoleDetailsView.as_view(), name='Role-update'),
    url(r'^class-list/$', CreateClassView.as_view(), name='Class-list'),
    url(r'^class-update/(?P<pk>[0-9]+)/$', ClassDetailsView.as_view(), name='Class-update'),
    url(r'^difficulty-list/$', DifficultyListCreateView.as_view(), name='Difficulty-list'),
    url(r'^difficulty-update/(?P<pk>[0-9]+)/$', DifficultyDetailsView.as_view(), name='Difficulty-update'),
    url(r'^boss-list/$', CreateBossView.as_view(), name='Boss-list'),
    url(r'^boss-update/(?P<pk>[0-9]+)/$', BossDetailsView.as_view(), name='Player-update'),
    url(r'^player-list/$', CreatePlayerView.as_view(), name='Boss-list'),
    url(r'^player-update/(?P<pk>[0-9]+)/$', PlayerDetailsView.as_view(), name='Player-update'),
}

urlpatterns = format_suffix_patterns(urlpatterns)