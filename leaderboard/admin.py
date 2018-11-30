from django.contrib import admin
from django import forms
from .models import *

class MatchlogForm(forms.ModelForm):
	winner = forms.ModelChoiceField(queryset=Player.objects.order_by('player_name'))
	loser = forms.ModelChoiceField(queryset=Player.objects.order_by('player_name'))
	
	class Meta:
		fields = '__all__'
		model = Matchlog
		
class MatchlogAdmin(admin.ModelAdmin):
	list_display = ('winner','loser','match_date')
	form = MatchlogForm
	
admin.site.register(Player)
admin.site.register(Matchlog, MatchlogAdmin)
admin.site.register(Ranks)