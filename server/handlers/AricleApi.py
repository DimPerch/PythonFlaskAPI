import time

from flask.views import MethodView
from flask import request
from ..app import db
from ..database.Article import Article


class ArticleApi(MethodView):
    def get(self):
        data = request.form.to_dict()
        _id = data.get('id')
        result = db.session.query(Article).get(int(_id))
        if result:
            return {"status": "ok", "result": result.to_json()}
        else:
            return {"status": "not found"}, 200

    def post(self):
        data = request.form.to_dict()
        article = Article(**data)
        article.time = time.time()
        db.session.add(article)
        db.session.commit()
        return {"status": "ok", "result": article.to_json()}, 200

    def put(self):
        data = request.form.to_dict()
        _id = data.get('id')
        status = Article.query.filter_by(id=_id).update(data)
        if status:
            db.session.commit()
            result = db.session.query(Article).get(int(_id))
            return {"status": "ok", "result": result.to_json()}
        else:
            return {"status": "not found"}, 200

    def delete(self):
        data = request.form.to_dict()
        _id = data.get('id', 0)
        Article.query.filter_by(id=_id).delete()
        db.session.commit()
        return {"status": "ok"}, 200
