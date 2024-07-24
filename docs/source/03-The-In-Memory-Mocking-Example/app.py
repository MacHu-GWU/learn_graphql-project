# -*- coding: utf-8 -*-

"""
This module convert graphene schema to Flask view. This capability is provided
by the flask_graphql package.
"""

from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)

app.add_url_rule(
    "/graphql",  # the final endpoint will be http://127.0.0.1:5000/graphql
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,
    ),
)

if __name__ == "__main__":
    app.run(debug=True)
