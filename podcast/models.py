from django.db import models

# Create your models here.
from djrichtextfield.models import RichTextField

from base.models import BaseModel, File, Category, Image
from shop.models import Product
from sort_order_field import SortOrderField


class Track(BaseModel):
    is_freemium = models.BooleanField(default=False)
    audio_file = models.OneToOneField(File, on_delete=models.CASCADE, blank=True, null=True)
    duration_seconds = models.IntegerField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    is_active = models.BooleanField(default=True)


class Podcast(BaseModel):
    categories = models.ManyToManyField(Category, blank=True, null=True)
    is_freemium = models.BooleanField(default=False)
    product = models.ForeignKey(Product, models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(Image, through='PodcastImage')
    tracks = models.ManyToManyField(Track, through='PodcastTrack')
    is_active = models.BooleanField(default=True)
    content = RichTextField()


class PodcastImage(models.Model):
    class Meta:
        ordering = ('order',)

    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    order = SortOrderField("Sort")


class PodcastTrack(models.Model):
    class Meta:
        ordering = ('order',)

    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    order = SortOrderField("Sort")
