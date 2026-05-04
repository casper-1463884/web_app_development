from datetime import datetime
from app import db
from .ingredient import Ingredient

# 食譜與食材的中間表
recipe_ingredients = db.Table('recipe_ingredients',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id', ondelete='CASCADE')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id', ondelete='CASCADE')),
    db.Column('amount', db.String(50), nullable=False),
    db.Column('unit', db.String(20), nullable=False)
)

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    instructions = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    prep_time = db.Column(db.Integer) # 分鐘
    cook_time = db.Column(db.Integer) # 分鐘
    servings = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯：多對多到食材
    ingredients = db.relationship('Ingredient', secondary=recipe_ingredients, lazy='subquery',
        backref=db.backref('recipes', lazy=True))

    def __repr__(self):
        return f'<Recipe {self.title}>'

    @staticmethod
    def create(title, instructions, user_id, **kwargs):
        """建立新食譜"""
        try:
            recipe = Recipe(title=title, instructions=instructions, user_id=user_id, **kwargs)
            db.session.add(recipe)
            db.session.commit()
            return recipe
        except Exception as e:
            db.session.rollback()
            print(f"Error creating recipe: {e}")
            return None

    @staticmethod
    def get_all():
        """取得所有食譜"""
        return Recipe.query.all()

    @staticmethod
    def get_by_id(recipe_id):
        """取得單一食譜"""
        return Recipe.query.get(recipe_id)

    def update(self, **kwargs):
        """更新食譜內容"""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating recipe: {e}")
            return False

    def delete(self):
        """刪除食譜"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting recipe: {e}")
            return False
