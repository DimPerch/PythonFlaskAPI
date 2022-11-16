from ..app import db
from ..app import app


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer(), primary_key=True)
    first_name = db.Column('first_name', db.String(200), nullable=False)
    last_name = db.Column('last_name', db.String(200), nullable=False)

    def to_json(self):
        return {"User": {"id": f"{self.id}",
                         "first_name": f"{self.first_name}",
                         "last_name": f"{self.last_name}"}}

    def __repr__(self):
        return str(self.to_json())

    def __str__(self):
        return self.__repr__()


with app.app_context():
    db.create_all()
