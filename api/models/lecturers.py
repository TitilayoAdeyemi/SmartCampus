from api.utils import db
from models.users import User


class Lecturer(User):
    __tablename__ = 'lecturer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    department = db.Column(db.String(), nullable = False)
    courses = db.relationship('Courses', backref='lecturer')

    def __repr__(self):
        return f'Lecturer {self.name}'
