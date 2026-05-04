from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    首頁儀表板。
    顯示今日菜單摘要、最近庫存提醒。
    """
    pass

@main_bp.route('/shopping-list')
def shopping_list():
    """
    顯示自動生成的購物清單。
    根據菜單所需與現有庫存計算。
    """
    pass
