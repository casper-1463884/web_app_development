from flask import Blueprint, render_template, request, redirect, url_for

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/')
def index():
    """
    瀏覽所有食譜。
    支援分類篩選與關鍵字搜尋。
    """
    pass

@recipes_bp.route('/<int:recipe_id>')
def detail(recipe_id):
    """
    顯示食譜詳情。
    包括步驟、食材清單與作者資訊。
    """
    pass

@recipes_bp.route('/new', methods=['GET'])
def new():
    """
    顯示新增食譜表單頁面。
    """
    pass

@recipes_bp.route('/', methods=['POST'])
def create():
    """
    接收表單資料並建立新食譜。
    處理食材關聯 (recipe_ingredients)。
    """
    pass

@recipes_bp.route('/<int:recipe_id>/edit', methods=['GET'])
def edit(recipe_id):
    """
    顯示食譜編輯頁面。
    """
    pass

@recipes_bp.route('/<int:recipe_id>/update', methods=['POST'])
def update(recipe_id):
    """
    接收編輯後的資料並更新資料庫。
    """
    pass

@recipes_bp.route('/<int:recipe_id>/delete', methods=['POST'])
def delete(recipe_id):
    """
    刪除特定食譜。
    """
    pass
