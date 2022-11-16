from ..app import db
from ..app import app


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column('article_id', db.Integer(), primary_key=True)
    title = db.Column('title', db.String(200), nullable=False)
    text = db.Column('text', db.Text(), nullable=False)
    author_id = db.Column('author_id', db.ForeignKey('users.user_id'), nullable=False)
    time = db.Column('time', db.DateTime(), nullable=False)

    def __repr__(self):
        return f'Article {self.title} {self.text}'

    def __str__(self):
        return str(self.__repr__())


with app.app_context():
    db.create_all()