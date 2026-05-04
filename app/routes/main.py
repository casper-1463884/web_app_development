from flask import Blueprint, render_template
from app.models.recipe import Recipe
from app.models.pantry import Pantry

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    首頁儀表板。
    顯示最近新增的食譜與庫存提醒（如即將到期的食材）。
    """
    recent_recipes = Recipe.get_all()[-5:] # 取得最近 5 筆
    pantry_items = Pantry.get_by_user(1) # 暫時用 User 1 測試
    return render_template('index.html', recipes=recent_recipes, pantry=pantry_items)

@main_bp.route('/shopping-list')
def shopping_list():
    """
    顯示自動生成的購物清單。
    邏輯：比對菜單需求與目前庫存（待後續實作詳細計算邏輯）。
    """
    # 這裡暫時回傳空列表，待 Menu 功能完成後整合
    return render_template('shopping_list.html', items=[])
