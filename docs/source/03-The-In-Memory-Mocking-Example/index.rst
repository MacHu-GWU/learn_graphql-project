The In Memory Mocking Example
==============================================================================


Overview
------------------------------------------------------------------------------
这篇文章介绍了如何用 graphene + flask + flask_graphql 实现一个极简的 GraphQL API. 这个例子中我们没有数据库, 而是用 in-memory 的 Python dict 来模拟数据存储后端.

.. note::

    这个例子是我自己写的, 在网上没有.


Code
------------------------------------------------------------------------------
resolver 模块定义了如何从后端中获取数据 (以后进阶的 dataloader 等高级模式都在这个模块中实现)

.. dropdown:: resolvers.py

    .. literalinclude:: ./resolvers.py
       :language: python
       :linenos:

schema 模块定义了 GraphQL 的 schema. 这个例子中只有 query 而没有 mutation.

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
