# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_guide', models.BooleanField(default=False)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('name', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('text', models.TextField(blank=True)),
                ('stars', models.IntegerField()),
                ('author', models.ForeignKey(related_name='authored_reviews', to='Guides.Profile')),
                ('subject', models.ForeignKey(to='Guides.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('capacity', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('price', models.FloatField()),
                ('guide', models.ForeignKey(related_name='guided_tours', to='Guides.Profile')),
                ('tourists', models.ManyToManyField(related_name='taken_tours', to='Guides.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
