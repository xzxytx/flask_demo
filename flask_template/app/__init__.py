from flask import Flask
# app = Flask(__name__)

# import app.views
# from app import views


def create_app(config_filename):
    app = Flask(__name__)

    # 从配置对象中为app设置配置信息, 只有大写名称的值才会被存储到配置对象中,配置文件
    app.config.from_pyfile(config_filename)

    from app.views.index import ho
    from app.views.admin import admin
    from app.views.frontend import bp
    app.register_blueprint(ho)
    app.register_blueprint(admin)
    app.register_blueprint(bp)

    return app
