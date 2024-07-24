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


query = """
{
  allEmployees {
    edges {
      node {
        id
        name
        department {
          name
        }
      }
    }
  }
}
""".strip()
rprint(run_query(query))
"""
This will print:

{
    'data': {
        'allEmployees': {
            'edges': [
                {
                    'node': {
                        'id': 'RW1wbG95ZWU6MQ==',
                        'name': 'Peter',
                        'department': {'name': 'Engineering'}
                    }
                },
                {
                    'node': {
                        'id': 'RW1wbG95ZWU6Mg==',
                        'name': 'Roy',
                        'department': {'name': 'Engineering'}
                    }
                },
                {
                    'node': {
                        'id': 'RW1wbG95ZWU6Mw==',
                        'name': 'Tracy',
                        'department': {'name': 'Human Resources'}
                    }
                }
            ]
        }
    }
}
"""
