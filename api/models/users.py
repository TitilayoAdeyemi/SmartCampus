from api.utils import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(), unique = True, nullable = False)
    password_hash = db.Column(db.Text(), nullable = False)
    roles = db.relationship('UserRole', backref='user')

    def __repr__(self):
        return f'{self.name}'
    

    def save(self):
        db.session.add(self)
        db.session.commit()


    
    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)

class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role = db.Column(db.String(20))

    def __repr__(self):
        return f'This user is a {self.role}'
