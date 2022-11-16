from ..app import db
from ..app import app


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column('comment_id', db.Integer(), primary_key=True)
    author_id = db.Column('author_id', db.ForeignKey('users.user_id'), nullable=False)
    article_id = db.Column('article_id', db.ForeignKey('articles.article_id'), nullable=False)
    text = db.Column('text', db.Text(), nullable=False)
    time = db.Column('time', db.DateTime(), nullable=False)

    def __repr__(self):
        return f'Comment {self.text}'

    def __str__(self):
        return self.__repr__()


with app.app_context():
    db.create_all()
