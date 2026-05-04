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
        item = Pantry(user_id=user_id, name=name, quantity=quantity, unit=unit, **kwargs)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def get_by_user(user_id):
        return Pantry.query.filter_by(user_id=user_id).all()

    def update_stock(self, new_quantity):
        self.quantity = new_quantity
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
