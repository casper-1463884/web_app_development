from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# 初始化 SQLAlchemy 物件
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # 設定資料庫路徑
    db_path = os.path.join(app.instance_path, 'database.db')
    
    # 基本配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{db_path}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # 確保 instance 資料夾存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 初始化外掛
    db.init_app(app)

    with app.app_context():
        # 匯入 Models 以確保 SQLAlchemy 註冊所有表與關聯
        from .models.user import User
        from .models.recipe import Recipe
        from .models.ingredient import Ingredient
        from .models.pantry import Pantry
        from .models.menu import MenuPlan

    # 註冊 Blueprints (路由)
    from .routes.main import main_bp
    from .routes.recipes import recipes_bp
    from .routes.menu import menu_bp
    from .routes.pantry import pantry_bp
    from .routes.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(pantry_bp)
    app.register_blueprint(api_bp)

    return app

def init_db():
    """初始化資料庫"""
    app = create_app()
    with app.app_context():
        # 必須匯入所有 Models 才能正確建立資料表
        from .models.user import User
        from .models.recipe import Recipe
        from .models.ingredient import Ingredient
        from .models.pantry import Pantry
        from .models.menu import MenuPlan
        
        db.create_all()
        print("資料庫初始化完成！")
