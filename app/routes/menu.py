from flask import Blueprint, render_template, request, redirect, url_for

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('/')
def index():
    """
    顯示每週菜單規劃表。
    以日曆或列表形式展示。
    """
    pass

@menu_bp.route('/add', methods=['POST'])
def add():
    """
    將特定食譜加入菜單計畫。
    參數: recipe_id, date, meal_type.
    """
    pass

@menu_bp.route('/<int:plan_id>/delete', methods=['POST'])
def remove(plan_id):
    """
    從菜單中移除特定餐次。
    """
    pass
