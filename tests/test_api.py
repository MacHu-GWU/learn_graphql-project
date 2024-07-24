# -*- coding: utf-8 -*-

from learn_graphql import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_graphql.tests import run_cov_test

    run_cov_test(__file__, "learn_graphql.api", preview=False)
