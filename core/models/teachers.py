from core import db
from core.libs import helpers
# import principal to teachers
from core.models.principals import Principal



class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # This line 
    # principal_id = db.Column(db.Integer, db.ForeignKey(Principal.id), nullable=True)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Teacher %r>' % self.id

# link up
    # @classmethod
    # def get_teacher_by_principal_id(cls, principal_id):
    #     return cls.filter(cls.id == principal_id).all()