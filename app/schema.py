import graphene

from base.schema import BaseQuery, BaseMutation
from podcast.schema import PodcastQuery
from shop.schema import ShopQuery, ShopMutation
from subscription.schema import SubscriptionQuery


class Query(
    BaseQuery,  # Add your Query objects here
    ShopQuery,
    PodcastQuery,
    SubscriptionQuery,
    graphene.ObjectType
):
    pass


class Mutation(BaseMutation, ShopMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
