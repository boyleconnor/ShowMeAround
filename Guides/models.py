from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import OneToOneField, ForeignKey, TextField, CharField, FloatField
from django.db.models.base import Model
from django.db.models.fields import BooleanField, IntegerField, DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField

User = get_user_model()


class Profile(Model):
    is_guide = BooleanField(default=False)
    user = OneToOneField(User)
    profile_picture = ImageField()
    name = TextField()

    def get_rating(self):
        return sum([float(review.stars) for review in self.reviews.all()]) / float(self.reviews.count())  # TODO: test this


class Tour(Model):
    title = TextField()
    description = TextField()

    guide = ForeignKey(Profile)
    tourists = ManyToManyField(Profile)
    capacity = IntegerField()

    start_time = DateTimeField()
    end_time = DateTimeField()

    latitude = FloatField()
    longitude = FloatField()

    price = FloatField()


class Review(Model):
    title = CharField(max_length=255, blank=True)
    text = TextField(blank=True)
    author = ForeignKey(Profile)
    subject = ForeignKey(Profile)
    stars = IntegerField()