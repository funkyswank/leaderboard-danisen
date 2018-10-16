from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from leaderboard.views import players

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^players/', players)
]