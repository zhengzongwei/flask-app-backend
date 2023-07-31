from flask import current_app, g
import click
import mariadb

from app.config import config


def get_db():
    db_config = config.get_config('mysql')
    if 'db' not in g:
        g.db = mariadb.connect(**db_config)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('./schema.sql', mode='r') as f:
        sql_context = f.read()
        sql_commands = sql_context.split(";")[:-1]

        for command in sql_commands:
            db.cursor().execute(command)
    db.commit()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
