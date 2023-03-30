from app import db, app


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127), unique=True)
    description = db.Column(db.String(255))
    date = db.Column(db.DateTime(timezone=True))

    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date

    def __repr__(self):
        return f'Task {self.title}'


with app.app_context():
    db.create_all()
