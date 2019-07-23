import asyncio

from flask import Flask
from flask_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor

from api.schema import schema

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# loop = asyncio.get_event_loop()

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
    executor=AsyncioExecutor(loop=loop)
))

# Optional, for adding batch query support (used in Apollo-Client)
app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql_batch', schema=schema, batch=True))

