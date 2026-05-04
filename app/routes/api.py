from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/recommend')
def recommend():
    """
    智慧推薦接口。
    根據當前使用者庫存回傳 JSON 格式的推薦食譜清單。
    """
    pass
