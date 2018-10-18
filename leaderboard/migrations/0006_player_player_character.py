# Generated by Django 2.1.2 on 2018-10-16 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0005_auto_20181016_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Character', to='leaderboard.Fighters'),
            preserve_default=False,
        ),
    ]