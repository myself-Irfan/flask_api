from app import init_app, db
from app.model import User, Post

app = init_app()

with app.app_context():
    print("Tables before create_all():", list(db.metadata.tables.keys()))
    db.create_all()
    print("Tables after create_all():", list(db.metadata.tables.keys()))
    print("Database initialized successfully")
