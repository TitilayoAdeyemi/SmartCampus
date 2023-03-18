from api.utils import db



class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    id = db.Column(db.Integer(), primary_key = True)
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id'), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id'), primary_key=True)

    def __repr__(self):
        return f'Student course {self.id}'
