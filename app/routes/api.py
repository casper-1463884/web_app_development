from flask import Blueprint, jsonify
from app.models.recipe import Recipe

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/recommend')
def recommend():
    """
    智慧推薦接口。
    根據當前使用者庫存回傳 JSON 格式的推薦食譜清單。
    """
    # 簡化邏輯：目前先推薦所有食譜
    recipes = Recipe.get_all()
    data = [{'id': r.id, 'title': r.title} for r in recipes]
    return jsonify(data)
