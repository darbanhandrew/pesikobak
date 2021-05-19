from django.contrib import admin
from django.apps import apps
from django_mptt_admin.admin import DjangoMpttAdmin
from graphql_jwt.refresh_token.models import RefreshToken
from payir.models import Transaction, Gateway

from podcast.models import  Podcast, PodcastTrack
from .models import Category

admin.site.register(Category, DjangoMpttAdmin)


class PodcastTrackInine(admin.TabularInline):
    model = PodcastTrack


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    inlines = (PodcastTrackInine,)


models = apps.get_models()

for model in models:
    if model == RefreshToken:
        continue
    if model == Category or model == Transaction or model == Gateway:
        continue
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
