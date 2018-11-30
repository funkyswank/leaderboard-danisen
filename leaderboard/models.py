import datetime
from django.db import models, transaction
from django.utils import timezone

class Fighters(models.Model):
	fighter = models.CharField(max_length=20)
	def __str__(self):
		return self.fighter

class Ranks(models.Model):
	rank = models.CharField(max_length=20)
	to_rank_up = models.IntegerField(default=3)
	to_rank_down = models.IntegerField(default=-3)
	def __str__(self):
		return self.rank

class Player(models.Model):
	player_name = models.CharField(max_length=50)
	player_character = models.ForeignKey(Fighters,on_delete=models.CASCADE,related_name='Character',default=1)
	player_rank = models.ForeignKey(Ranks,on_delete=models.CASCADE,related_name='Ranking',default=1)
	player_points = models.IntegerField(default=0)
	def __str__(self):
		return self.player_name+" - "+str(self.player_character)+" - "+str(self.player_rank)+" "+str(self.player_points)

class Matchlog(models.Model):
	winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner')
	loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='loser')
	match_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return str(self.winner)+" - "+str(self.winner.player_character)+" beat "+str(self.loser)+" - "+str(self.loser.player_character)+" on "+str(self.match_date)
	@transaction.atomic
	def save(self):
		if self.pk is None:
			game = super().save()
			self.winner.player_points += 1
			if self.winner.player_points >= self.winner.player_rank.to_rank_up:
				self.winner.player_rank_id += 1
				self.winner.player_points = 0
			self.winner.save()
			if self.loser.player_rank_id == 1 and self.loser.player_points == 0:
				pass
			else:
				self.loser.player_points -=1
				if self.loser.player_points <= self.loser.player_rank.to_rank_down:
					self.loser.player_points = 0
					self.loser.player_rank_id -= 1
			self.loser.save()
			return game