# -*- coding: utf-8 -*-

"""
This module implements resolvers.
"""

import typing as T


class UserType(T.TypedDict):
    id: str
    name: str
    email: str


def resolve_users():
    # Mock data
    return [
        {"id": "1", "name": "Alice", "email": "alice@example.com"},
        {"id": "2", "name": "Bob", "email": "bob@example.com"},
        {"id": "3", "name": "Charlie", "email": "charlie@example.com"},
    ]


def resolve_user_by_id(id: str) -> UserType:
    users = resolve_users()
    return next((user for user in users if user["id"] == id), None)
