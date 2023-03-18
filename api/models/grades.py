from api.utils import db

class Grades(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id'), nullable=False)
    grade = db.Column(db.String(), nullable = False )

    def __repr__(self):
        return f'{self.grade}'