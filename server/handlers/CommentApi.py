from flask.views import MethodView
from flask import request
from ..app import db
from ..database.Comment import Comment
import time


class CommentApi(MethodView):
    def get(self):
        data = request.form.to_dict()
        _id = data.get('id')
        result = db.session.query(Comment).get(int(_id))
        if result:
            return {"status": "ok", "result": result.to_json()}
        else:
            return {"status": "not found"}, 200

    def post(self):
        data = request.form.to_dict()
        comment = Comment(**data)
        comment.time = time.time()
        db.session.add(comment)
        db.session.commit()
        return {"status": "ok", "result": comment.to_json()}, 200

    def put(self):
        data = request.form.to_dict()
        _id = data.get('id')
        status = Comment.query.filter_by(id=_id).update(data)
        if status:
            db.session.commit()
            result = db.session.query(Comment).get(int(_id))
            return {"status": "ok", "result": result.to_json()}
        else:
            return {"status": "not found"}, 200

    def delete(self):
        data = request.form.to_dict()
        _id = data.get('id', 0)
        Comment.query.filter_by(id=_id).delete()
        db.session.commit()
        return {"status": "ok"}, 200
