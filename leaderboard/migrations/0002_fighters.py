# Generated by Django 2.1.2 on 2018-10-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fighters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fighter', models.CharField(max_length=20)),
            ],
        ),
    ]
