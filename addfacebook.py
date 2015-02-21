from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
SocialApp.objects.create(provider="facebook", name="Facebook", secret="ce2851bc034b88009817f13aa2d4b48e", client_id="1605539486334838", key='')
facebook = SocialApp.objects.get()
facebook.sites.add(Site.objects.get(id=1))
facebook.save()
