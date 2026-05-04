from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.pantry import Pantry

pantry_bp = Blueprint('pantry', __name__, url_prefix='/pantry')

@pantry_bp.route('/')
def index():
    """顯示個人食材庫存清單"""
    items = Pantry.get_by_user(1) # 暫時用 User 1
    return render_template('pantry/index.html', items=items)

@pantry_bp.route('/update', methods=['POST'])
def update():
    """更新或新增庫存項目"""
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    unit = request.form.get('unit')
    
    if not name or not quantity or not unit:
        flash("名稱、數量與單位為必填", "warning")
        return redirect(url_for('pantry.index'))
    
    try:
        quantity = float(quantity)
    except ValueError:
        flash("數量格式錯誤", "danger")
        return redirect(url_for('pantry.index'))

    # 檢查是否已有該項目（簡化邏輯：依名稱判斷）
    item = Pantry.query.filter_by(user_id=1, name=name).first()
    if item:
        item.update_stock(quantity=quantity, unit=unit)
        flash(f"已更新 {name} 庫存", "success")
    else:
        Pantry.add_item(user_id=1, name=name, quantity=quantity, unit=unit)
        flash(f"已新增 {name} 至庫存", "success")
        
    return redirect(url_for('pantry.index'))
