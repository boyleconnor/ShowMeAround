from django.contrib.auth.models import User
from django.db.models import OneToOneField, ForeignKey, TextField, CharField, FloatField
from django.db.models.base import Model
from django.db.models.fields import BooleanField, IntegerField, DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField


class Profile(Model):
    is_guide = BooleanField(default=False)
    user = OneToOneField(User)
    profile_picture = ImageField()
    name = TextField()

    def get_rating(self):
        return sum([float(review.stars) for review in self.reviews.all()]) / float(self.reviews.count())  # TODO: test this

    def __str__(self):
        return ('Guide - %s' if self.is_guide else 'Tourist - %s') % self.name


class Tour(Model):
    title = TextField()
    description = TextField()

    guide = ForeignKey(Profile, related_name='guided_tours')
    tourists = ManyToManyField(blank=True, Profile, related_name='taken_tours')
    capacity = IntegerField()

    start_time = DateTimeField()
    end_time = DateTimeField()

    latitude = FloatField()
    longitude = FloatField()

    price = FloatField()


class Review(Model):
    title = CharField(max_length=255, blank=True)
    text = TextField(blank=True)
    author = ForeignKey(Profile, related_name='authored_reviews')
    subject = ForeignKey(Profile)
    stars = IntegerField()