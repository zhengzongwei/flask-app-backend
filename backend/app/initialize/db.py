import click
from app.common.common import db
from app.models.book import Books, Publish
from app.config.constants import PUBLISH
from flask_babel import gettext as _


def init_app(app):
    app.cli.add_command(init_db_command)


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo(_('Initialized the database.'))


def init_db():
    print("sadf")
    init_publish = []
    for _publish in PUBLISH:
        print(_publish['name'])
        init_publish.append(Publish(name=_publish['name']))
    try:
        db.session.add_all(init_publish)
        db.session.commit()
    except Exception as e:
        print("123", e)
        db.session.rollback()
