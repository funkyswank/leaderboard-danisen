# Generated by Django 2.1.2 on 2018-10-16 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_auto_20181016_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ranking', to='leaderboard.Ranks'),
        ),
    ]