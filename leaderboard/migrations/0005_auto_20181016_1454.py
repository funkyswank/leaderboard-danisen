# Generated by Django 2.1.2 on 2018-10-16 19:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0004_auto_20181016_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchlog',
            name='match_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_rank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Ranking', to='leaderboard.Ranks'),
        ),
    ]
