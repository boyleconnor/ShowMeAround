from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import ForeignKey, TextField, CharField, FloatField, ImageField
from django.db.models.base import Model
from django.db.models.fields import BooleanField, IntegerField, DateTimeField, EmailField
from django.db.models.fields.related import ManyToManyField


class Language(Model):
    english_name = CharField(max_length=50)
    native_name = CharField(max_length=50)

    def get_name_display(self):
        if self.english_name != self.native_name:
            return '%s / %s' % (self.english_name, self.native_name)
        else:
            return self.english_name

    def __str__(self):
        return self.get_name_display()


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', ]

    languages = ManyToManyField(Language, null=True, blank=True)
    objects = UserManager()
    username = CharField(unique=True, max_length=30)
    email = EmailField(unique=True)
    name = CharField(max_length=100, blank=True)
    profile_picture = ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_guide = BooleanField(default=False)
    date_joined = DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_best_identifier(self):
        return self.name if self.name else self.username

    def get_absolute_url(self):
        return self.get_detail_url()

    def get_detail_url(self):
        return reverse_lazy('guides:user.detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('guides:user.edit', kwargs={'pk': self.pk})

    def get_rating(self):
        if self.reviews.count():
            return sum([float(review.stars) for review in self.reviews.all()]) / float(self.reviews.count())  # TODO: test this
        else:
            return None

    def __str__(self):
        return ('Guide - %s' if self.is_guide else 'Tourist - %s') % self.name


class Tour(Model):
    title = TextField()
    description = TextField(help_text="On the description, please specify the general location(s) of the tour and ways to contact you. ")
    language = ForeignKey(Language, blank=True, null=True)

    guide = ForeignKey(User, related_name='guided_tours')
    tourists = ManyToManyField(User, related_name='taken_tours', blank=True)
    capacity = IntegerField()

    start_time = DateTimeField()
    end_time = DateTimeField()

    latitude = FloatField()
    longitude = FloatField()

    price = FloatField()

    def get_detail_url(self):
        return reverse_lazy('guides:tour.detail', kwargs={'pk': self.pk})

    def get_join_url(self):
        return reverse_lazy('guides:tour.join', kwargs={'pk': self.pk})

    def get_leave_url(self):
        return reverse_lazy('guides:tour.leave', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return self.get_detail_url()

    def __str__(self):
        return self.title


class Review(Model):
    class Meta:
        unique_together = ('author', 'tour')
    title = CharField(max_length=255, blank=True)
    text = TextField(blank=True)
    author = ForeignKey(User, related_name='authored_reviews')
    tour = ForeignKey(Tour, related_name='reviews')
    subject = ForeignKey(User)
    stars = IntegerField()

    def __str__(self):
        return self.title
