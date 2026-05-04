from datetime import datetime
from app import db

class MenuPlan(db.Model):
    __tablename__ = 'menu_plans'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id', ondelete='CASCADE'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    meal_type = db.Column(db.String(20), nullable=False) # Breakfast, Lunch, Dinner, Snack
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯到食譜
    recipe = db.relationship('Recipe', backref='planned_in', lazy=True)

    def __repr__(self):
        return f'<MenuPlan {self.date} {self.meal_type}>'

    @staticmethod
    def create_plan(user_id, recipe_id, date, meal_type):
        plan = MenuPlan(user_id=user_id, recipe_id=recipe_id, date=date, meal_type=meal_type)
        db.session.add(plan)
        db.session.commit()
        return plan

    @staticmethod
    def get_by_date_range(user_id, start_date, end_date):
        return MenuPlan.query.filter(
            MenuPlan.user_id == user_id,
            MenuPlan.date >= start_date,
            MenuPlan.date <= end_date
        ).order_by(MenuPlan.date, MenuPlan.meal_type).all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
