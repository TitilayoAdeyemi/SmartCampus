from api.utils import db

class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer(), primary_key=True)
    lecturer_name = db.Column(db.String(), nullable = False)
    # lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'))
    course_code = db.Column(db.String(40), nullable=False) #Also known as the course name
    course_description = db.Column(db.String(), nullable = False)
    course_unit = db.Column(db.Integer(), nullable = False)
    grades = db.Column(db.String(), nullable = False)
    student = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'Course {self.course_code}'
    

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    
    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)