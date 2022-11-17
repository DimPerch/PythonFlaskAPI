from server.app import app
from server.handlers.UserApi import UserApi
from server.handlers.AricleApi import ArticleApi
from server.handlers.CommentApi import CommentApi


API_URL = '/api/v1.0'


def main():
    app.add_url_rule(f'{API_URL}/users/', view_func=UserApi.as_view('users'))
    app.add_url_rule(f'{API_URL}/articles/', view_func=ArticleApi.as_view('articles'))
    app.add_url_rule(f'{API_URL}/comments/', view_func=CommentApi.as_view('comments'))
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
