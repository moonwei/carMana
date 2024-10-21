from flask import Flask, render_template
from flask_migrate import Migrate
from extensions import db, init_db
from routes import camera, whitelist, status, recognition, statistics, gate
import models  # 导入 models 模块

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)  # 添加这行

    # 注册路由
    app.register_blueprint(camera.bp)
    app.register_blueprint(whitelist.bp)
    app.register_blueprint(status.bp)
    app.register_blueprint(recognition.bp)
    app.register_blueprint(statistics.bp)
    app.register_blueprint(gate.bp)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
