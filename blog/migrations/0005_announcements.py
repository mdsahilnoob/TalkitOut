# Generated by Django 3.2.9 on 2022-12-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221206_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='TITLE', max_length=50)),
                ('announce', models.TextField(max_length=200)),
            ],
        ),
    ]
