from app import create_app
from app import db
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from app.models import user
        db.create_all()

    app.run(debug=True)