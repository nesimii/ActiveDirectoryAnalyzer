import os

from neomodel import config


def connect_neo4j():
    bolt_url = os.environ.get('neo4j_bolt_url', 'localhost')
    port = os.environ.get('neo4j_bolt_port', '7687')
    username = os.environ.get('neo4j_username', 'neo4j')
    password = os.environ.get('neo4j_password', 'password')
    config.DATABASE_URL = f"bolt://{username}:{password}@{bolt_url}:{port}"
