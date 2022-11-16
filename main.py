from server.app import app
from server.handlers.UserApi import UserApi


API_URL = '/api/v1.0'


def main():
    app.add_url_rule(f'{API_URL}/users/', view_func=UserApi.as_view('users'))
    app.run()


if __name__ == '__main__':
    main()
