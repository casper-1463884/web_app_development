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
        """建立菜單計畫"""
        try:
            plan = MenuPlan(user_id=user_id, recipe_id=recipe_id, date=date, meal_type=meal_type)
            db.session.add(plan)
            db.session.commit()
            return plan
        except Exception as e:
            db.session.rollback()
            print(f"Error creating menu plan: {e}")
            return None

    @staticmethod
    def get_by_id(plan_id):
        """取得單一菜單計畫"""
        return MenuPlan.query.get(plan_id)

    @staticmethod
    def get_by_date_range(user_id, start_date, end_date):
        """取得特定日期範圍內的菜單計畫"""
        return MenuPlan.query.filter(
            MenuPlan.user_id == user_id,
            MenuPlan.date >= start_date,
            MenuPlan.date <= end_date
        ).order_by(MenuPlan.date, MenuPlan.meal_type).all()

    def delete(self):
        """刪除菜單計畫"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting menu plan: {e}")
            return False
