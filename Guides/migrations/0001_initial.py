# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(blank=True, max_length=255)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('profile_picture', models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Profile Pic')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_guide', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(to='auth.Group', related_query_name='user', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, verbose_name='groups')),
                ('languages', models.ManyToManyField(to='Guides.Language', blank=True, null=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_query_name='user', related_name='user_set', help_text='Specific permissions for this user.', blank=True, verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tour',
            name='guide',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='guided_tours'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tour',
            name='language',
            field=models.ForeignKey(to='Guides.Language', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tour',
            name='tourists',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='taken_tours', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='authored_reviews'),
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
            field=models.ForeignKey(to='Guides.Tour', related_name='reviews'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('author', 'tour')]),
        ),
    ]
