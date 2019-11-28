from flask_cors import CORS
from mainapp import app
from mainapp.views import function_api,user_api,name_test_api,gift_api,change_password_api,attention_api

if __name__ == '__main__':
    app.register_blueprint(function_api.user_function_blue, url_prefix='/function')
    app.register_blueprint(user_api.user_blue, url_prefix='/user')
    app.register_blueprint(name_test_api.test_blue,url_prefix='/name')
    app.register_blueprint(gift_api.gift_blue,url_prefix='/live')
    app.register_blueprint(change_password_api.change_blue,url_prefix='/change')
    app.register_blueprint(attention_api.my_blue, url_prefix='/Attention/')
    CORS(app)
    app.run('0.0.0.0', 8080)