from django_filters import OrderingFilter
from graphene import relay, ObjectType, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


class TrackNode(DjangoObjectType):
    class Meta:
        model = Track
        filter_fields = ['id', 'title', 'is_active', 'categories']
        interfaces = (relay.Node,)


class PodcastNode(DjangoObjectType):
    class Meta:
        model = Podcast
        filter_fields = ['id', 'title', 'is_active', 'categories']
        interfaces = (relay.Node,)


class PodcastImageNode(DjangoObjectType):
    class Meta:
        model = PodcastImage
        filter_fields = ['id', 'is_featured']
        order_by = OrderingFilter(
            fields=(
                'order',
            )
        )
        interfaces = (relay.Node,)


class PodcastTrackNode(DjangoObjectType):
    class Meta:
        model = PodcastTrack
        filter_fields = ['id', 'podcast']
        order_by = OrderingFilter(
            fields=(
                'order',
            )
        )
        interfaces = (relay.Node,)


class PodcastQuery(ObjectType):
    podcast = relay.Node.Field(PodcastNode)
    all_podcasts = DjangoFilterConnectionField(PodcastNode)

    track = relay.Node.Field(TrackNode)
    all_tracks = DjangoFilterConnectionField(TrackNode)

    podcast_image = relay.Node.Field(PodcastImageNode)
    all_podcast_images = DjangoFilterConnectionField(PodcastImageNode)

    podcast_track = relay.Node.Field(PodcastTrackNode)
    all_podcast_tracks = DjangoFilterConnectionField(PodcastTrackNode)
