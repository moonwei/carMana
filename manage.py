from flask.cli import FlaskGroup
from app import create_app
from extensions import db
from models import Camera, Whitelist, Recognition
from flask_migrate import Migrate, upgrade

app = create_app()
cli = FlaskGroup(create_app=create_app)
migrate = Migrate(app, db)

@cli.command("create_db")
def create_db():
    db.create_all()
    print("Database tables created")

@cli.command("db_migrate")
def db_migrate():
    with app.app_context():
        upgrade()
    print("Database migrated")

if __name__ == '__main__':
    cli()
