# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('english_name', models.CharField(max_length=50)),
                ('native_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('text', models.TextField(blank=True)),
                ('stars', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.TextField()),
                ('description', models.TextField(help_text='On the description, please specify the general location(s) of the tour and ways to contact you. ')),
                ('capacity', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('price', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_guide', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_name='user_set', verbose_name='groups', to='auth.Group', related_query_name='user')),
                ('languages', models.ManyToManyField(null=True, to='Guides.Language', blank=True)),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', blank=True, related_name='user_set', verbose_name='user permissions', to='auth.Permission', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tour',
            name='guide',
            field=models.ForeignKey(related_name='guided_tours', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tour',
            name='language',
            field=models.ForeignKey(null=True, blank=True, to='Guides.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tour',
            name='tourists',
            field=models.ManyToManyField(related_name='taken_tours', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(related_name='authored_reviews', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='tour',
            field=models.ForeignKey(related_name='reviews', to='Guides.Tour'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('author', 'tour')]),
        ),
    ]
