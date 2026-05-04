from datetime import datetime
from app import db # 假設 app/__init__.py 會初始化 db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    recipes = db.relationship('Recipe', backref='author', lazy=True)
    pantry_items = db.relationship('Pantry', backref='owner', lazy=True)
    menu_plans = db.relationship('MenuPlan', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    @staticmethod
    def create(username, password_hash, email):
        """
        建立新使用者。
        :param username: 帳號名稱
        :param password_hash: 加密後的密碼
        :param email: 電子郵件
        :return: User 物件或 None
        """
        try:
            user = User(username=username, password_hash=password_hash, email=email)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {e}")
            return None

    @staticmethod
    def get_by_id(user_id):
        """取得單一使用者"""
        return User.query.get(user_id)

    @staticmethod
    def get_all():
        """取得所有使用者"""
        return User.query.all()

    def update(self, **kwargs):
        """
        更新使用者資料。
        """
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating user: {e}")
            return False

    def delete(self):
        """
        刪除使用者。
        """
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting user: {e}")
            return False
