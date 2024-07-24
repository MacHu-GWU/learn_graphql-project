# -*- coding: utf-8 -*-

"""
This module defines the GraphQL schema.
"""

import graphene
from resolvers import resolve_users, resolve_user_by_id


class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, id=graphene.ID(required=True))

    def resolve_users(self, info):
        print(info)
        return resolve_users()

    def resolve_user(self, info, id: str):
        print(info)
        return resolve_user_by_id(id)


schema = graphene.Schema(query=Query)
