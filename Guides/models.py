from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import ForeignKey, TextField, CharField, FloatField
from django.db.models.base import Model
from django.db.models.fields import BooleanField, IntegerField, DateTimeField, EmailField
from django.db.models.fields.related import ManyToManyField


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', ]

    objects = UserManager()
    username = CharField(unique=True, max_length=30)
    email = EmailField(unique=True)
    name = CharField(max_length=100, blank=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    date_joined = DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_best_identifier(self):
        return self.name if self.name else self.username

    def get_absolute_url(self):
        return reverse_lazy('couches:profile.detail', kwargs={'username': self.username})

    def get_rating(self):
        return sum([float(review.stars) for review in self.reviews.all()]) / float(
            self.reviews.count())  # TODO: test this

    def get_update_url(self):
        return reverse_lazy('profile.edit', kwargs={'pk': self.pk})

    def __str__(self):
        return ('Guide - %s' if self.is_guide else 'Tourist - %s') % self.name


class Tour(Model):
    title = TextField()
    description = TextField()

    guide = ForeignKey(User, related_name='guided_tours')
    tourists = ManyToManyField(User, related_name='taken_tours', blank=True)
    capacity = IntegerField()

    start_time = DateTimeField()
    end_time = DateTimeField()

    latitude = FloatField()
    longitude = FloatField()

    price = FloatField()


class Review(Model):
    title = CharField(max_length=255, blank=True)
    text = TextField(blank=True)
    author = ForeignKey(User, related_name='authored_reviews')
    subject = ForeignKey(User)
    stars = IntegerField()