from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.menu import MenuPlan
from datetime import datetime

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('/')
def index():
    """顯示每週菜單規劃表"""
    # 預設顯示本週計畫
    plans = MenuPlan.get_by_date_range(1, datetime.now(), datetime.now()) # 簡化：僅今日
    return render_template('menu/index.html', plans=plans)

@menu_bp.route('/add', methods=['POST'])
def add():
    """將特定食譜加入菜單計畫"""
    recipe_id = request.form.get('recipe_id')
    date_str = request.form.get('date')
    meal_type = request.form.get('meal_type')
    
    if not recipe_id or not date_str or not meal_type:
        flash("請完整填寫計畫資訊", "warning")
        return redirect(url_for('menu.index'))
    
    try:
        plan_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        MenuPlan.create_plan(user_id=1, recipe_id=int(recipe_id), date=plan_date, meal_type=meal_type)
        flash("已成功加入菜單！", "success")
    except Exception as e:
        flash(f"計畫加入失敗: {e}", "danger")
        
    return redirect(url_for('menu.index'))

@menu_bp.route('/<int:plan_id>/delete', methods=['POST'])
def remove(plan_id):
    """從菜單中移除特定餐次"""
    plan = MenuPlan.get_by_id(plan_id)
    if plan and plan.delete():
        flash("已從菜單移除", "info")
    else:
        flash("移除失敗", "danger")
    return redirect(url_for('menu.index'))
