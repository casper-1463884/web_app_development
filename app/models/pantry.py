from datetime import datetime
from app import db

class Pantry(db.Model):
    __tablename__ = 'pantry'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    quantity = db.Column(db.Float, nullable=False, default=0.0)
    unit = db.Column(db.String(20), nullable=False)
    expiry_date = db.Column(db.Date)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Pantry {self.name} ({self.quantity} {self.unit})>'

    @staticmethod
    def add_item(user_id, name, quantity, unit, **kwargs):
        """新增食材庫存項目"""
        try:
            item = Pantry(user_id=user_id, name=name, quantity=quantity, unit=unit, **kwargs)
            db.session.add(item)
            db.session.commit()
            return item
        except Exception as e:
            db.session.rollback()
            print(f"Error adding pantry item: {e}")
            return None

    @staticmethod
    def get_by_user(user_id):
        """取得特定使用者的所有庫存"""
        return Pantry.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(item_id):
        """取得單一庫存項目"""
        return Pantry.query.get(item_id)

    def update_stock(self, **kwargs):
        """更新庫存數量或其他資訊"""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating pantry item: {e}")
            return False

    def delete(self):
        """刪除庫存項目"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting pantry item: {e}")
            return False
