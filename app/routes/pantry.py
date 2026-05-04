from flask import Blueprint, render_template, request, redirect, url_for

pantry_bp = Blueprint('pantry', __name__, url_prefix='/pantry')

@pantry_bp.route('/')
def index():
    """
    顯示個人食材庫存清單。
    標示數量、單位與剩餘效期。
    """
    pass

@pantry_bp.route('/update', methods=['POST'])
def update():
    """
    更新或新增庫存項目。
    支援批量更新或單項調整。
    """
    pass
