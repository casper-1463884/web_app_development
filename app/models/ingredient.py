from app import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(50))

    def __repr__(self):
        return f'<Ingredient {self.name}>'

    @staticmethod
    def get_or_create(name, category=None):
        ingredient = Ingredient.query.filter_by(name=name).first()
        if not ingredient:
            ingredient = Ingredient(name=name, category=category)
            db.session.add(ingredient)
            db.session.commit()
        return ingredient

    @staticmethod
    def get_all():
        return Ingredient.query.all()
