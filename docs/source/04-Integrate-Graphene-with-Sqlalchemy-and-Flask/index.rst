Integrate Graphene with Sqlalchemy and Flask
==============================================================================

Overview
------------------------------------------------------------------------------
这篇文章介绍了如何用 graphene + flask + flask_graphql + sqlalchemy + graphene_sqlalchemy 实现一个极简但跟生产环境的代码很类似的的 GraphQL API. 这个例子中我们用 sqlite 做数据库

.. note::

    这个例子来自于 https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/


Code
------------------------------------------------------------------------------
models 模块定义了 sqlalchemy ORM 的模型.

.. dropdown:: models.py

    .. literalinclude:: ./models.py
       :language: python
       :linenos:

运行 ``add_some_data.py`` 脚本可以往数据库中添加一些测试用的数据.

.. dropdown:: models.py

    .. literalinclude:: ./models.py
       :language: python
       :linenos:

schema 模块定义了 GraphQL 的 schema. ``graphene_sqlalchemy`` 库能够自动将 sqlalchemy ORM 对象转化为 graphql 对象, 并且自动实现了对应的 resolver, 而无需你手动实现.

.. dropdown:: schema.py

    .. literalinclude:: ./schema.py
       :language: python
       :linenos:

app 模块将 graphql 的部分和 flask 的部分结合在一起.

.. dropdown:: app.py

    .. literalinclude:: ./schema.py
       :language: python
       :linenos:


Test
------------------------------------------------------------------------------
我们写了个简单的脚本, 用于测试在 localhost 运行的 GraphQL API Server.

.. dropdown:: test.py

    .. literalinclude:: ./test.py
       :language: python
       :linenos:



Reference
------------------------------------------------------------------------------
- https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/
