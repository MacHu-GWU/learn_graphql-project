# -*- coding: utf-8 -*-

import requests
from rich import print as rprint


def run_query(query: str) -> dict:
    res = requests.post(
        "http://127.0.0.1:5000/graphql",
        headers={
            "Content-Type": "application/json",
        },
        json={"query": query.strip()},
    )
    return res.json()


# Put your graphql query here
query1 = """
{
  users {
    id
    name
    email
  }
}
"""
rprint(run_query(query1))
"""
Will print:

{
    'data': {
        'users': [
            {'id': '1', 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': '2', 'name': 'Bob', 'email': 'bob@example.com'},
            {'id': '3', 'name': 'Charlie', 'email': 'charlie@example.com'}
        ]
    }
}
"""

query2 = """
{
  user(id: "1") {
    id
    name
    email
  }
}
"""
rprint(run_query(query2))
"""
Will print:

{'data': {'user': {'id': '1', 'name': 'Alice', 'email': 'alice@example.com'}}}
"""
