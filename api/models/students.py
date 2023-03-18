from api.utils import db
from .users import User

class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer(), db.ForeignKey('user.id'), primary_key=True)
    student_name = db.Column(db.String(50))
    student_email = db.Column(db.String(), unique = True, nullable = False)
    department = db.Column(db.String(), nullable = False)
    matric_no = db.Column(db.Integer(), nullable = False)
    courses = db.relationship('Courses', secondary='student_course', backref='student')
    grade = db.relationship('Grades', backref='student_grade', lazy=True)

    

    def __repr__(self):
        return f'{self.name}'
    
    
