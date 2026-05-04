from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.menu import MenuPlan
from app.models.recipe import Recipe
from datetime import datetime, timedelta

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('/')
def index():
    """
    顯示每週菜單規劃表。
    """
    # 取得本週的計畫 (今天起算 7 天)
    today = datetime.now().date()
    start_date = today
    end_date = start_date + timedelta(days=7)
    
    plans = MenuPlan.get_by_date_range(user_id=1, start_date=start_date, end_date=end_date)
    all_recipes = Recipe.get_all()
    
    return render_template('menu/index.html', plans=plans, recipes=all_recipes, today=today.strftime('%Y-%m-%d'))

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
        # 去除空白並嘗試解析
        date_str = date_str.strip()
        plan_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        MenuPlan.create_plan(
            user_id=1, 
            recipe_id=int(recipe_id), 
            date=plan_date, 
            meal_type=meal_type
        )
        flash("已成功將食譜加入菜單！", "success")
    except ValueError as e:
        flash(f"日期格式錯誤 ({date_str})，請使用 YYYY-MM-DD", "danger")
    except Exception as e:
        flash(f"加入計畫時發生錯誤: {str(e)}", "danger")
        
    return redirect(url_for('menu.index'))

@menu_bp.route('/<int:plan_id>/delete', methods=['POST'])
def remove(plan_id):
    """從菜單中移除特定餐次"""
    plan = MenuPlan.get_by_id(plan_id)
    if not plan:
        flash("找不到該計畫紀錄", "warning")
        return redirect(url_for('menu.index'))
        
    if plan.delete():
        flash("已成功從菜單移除", "info")
    else:
        flash("移除失敗", "danger")
        
    return redirect(url_for('menu.index'))
