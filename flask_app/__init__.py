from flask import Flask
from flask_graphql import GraphQLView
from schema import sale_point_schema


def create_app():
    app = Flask(__name__)

    app.add_url_rule(
        '/sale_point',
        view_func=GraphQLView.as_view(
            'sale_point',
            schema=sale_point_schema,
            graphiql=True
        )
    )

    return app

