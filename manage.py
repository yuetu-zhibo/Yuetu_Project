from flask_cors import CORS
from mainapp import app
from mainapp.views import function_api, user_api, name_test_api, gift_api, change_password_api, attention_api, \
    intereted_api, start_live_api


def make_app():
    app.register_blueprint(function_api.user_function_blue, url_prefix='/api')
    app.register_blueprint(user_api.user_blue, url_prefix='/api/user')
    app.register_blueprint(name_test_api.test_blue,url_prefix='/api/name')
    app.register_blueprint(gift_api.gift_blue,url_prefix='/api/live')
    app.register_blueprint(change_password_api.change_blue,url_prefix='/api/change')
    app.register_blueprint(attention_api.my_blue, url_prefix='/api/Attention/')
    app.register_blueprint(intereted_api.feel_blue,url_prefix='/api/feel')
    app.register_blueprint(start_live_api.start_blue, url_prefix='/api/start')

    CORS(app)
    return app

application = make_app()

if __name__ == '__main__':
    application.run('0.0.0.0', 8080)