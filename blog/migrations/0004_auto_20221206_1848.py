# Generated by Django 3.2.9 on 2022-12-06 13:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(related_name='post_vote', to=settings.AUTH_USER_MODEL),
        ),
    ]
