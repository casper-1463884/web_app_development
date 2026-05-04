from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.recipe import Recipe

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/')
def index():
    """瀏覽所有食譜"""
    recipes = Recipe.get_all()
    return render_template('recipes/index.html', recipes=recipes)

@recipes_bp.route('/<int:recipe_id>')
def detail(recipe_id):
    """顯示食譜詳情"""
    recipe = Recipe.get_by_id(recipe_id)
    if not recipe:
        flash("找不到該食譜", "danger")
        return redirect(url_for('recipes.index'))
    return render_template('recipes/detail.html', recipe=recipe)

@recipes_bp.route('/new', methods=['GET'])
def new():
    """顯示新增食譜表單"""
    return render_template('recipes/new.html')

@recipes_bp.route('/', methods=['POST'])
def create():
    """建立新食譜"""
    title = request.form.get('title')
    instructions = request.form.get('instructions')
    description = request.form.get('description')
    
    if not title or not instructions:
        flash("標題與步驟為必填項目", "warning")
        return redirect(url_for('recipes.new'))
    
    # 這裡暫時預設 user_id 為 1
    recipe = Recipe.create(title=title, instructions=instructions, description=description, user_id=1)
    
    if recipe:
        flash("食譜新增成功！", "success")
        return redirect(url_for('recipes.detail', recipe_id=recipe.id))
    else:
        flash("新增失敗，請稍後再試", "danger")
        return redirect(url_for('recipes.new'))

@recipes_bp.route('/<int:recipe_id>/edit', methods=['GET'])
def edit(recipe_id):
    """顯示編輯頁面"""
    recipe = Recipe.get_by_id(recipe_id)
    if not recipe:
        flash("找不到食譜", "danger")
        return redirect(url_for('recipes.index'))
    return render_template('recipes/edit.html', recipe=recipe)

@recipes_bp.route('/<int:recipe_id>/update', methods=['POST'])
def update(recipe_id):
    """更新食譜"""
    recipe = Recipe.get_by_id(recipe_id)
    if not recipe:
        flash("找不到食譜", "danger")
        return redirect(url_for('recipes.index'))
    
    title = request.form.get('title')
    instructions = request.form.get('instructions')
    
    if not title or not instructions:
        flash("標題與步驟為必填", "warning")
        return redirect(url_for('recipes.edit', recipe_id=recipe_id))
    
    success = recipe.update(
        title=title, 
        instructions=instructions, 
        description=request.form.get('description')
    )
    
    if success:
        flash("食譜更新成功", "success")
    else:
        flash("更新失敗", "danger")
        
    return redirect(url_for('recipes.detail', recipe_id=recipe_id))

@recipes_bp.route('/<int:recipe_id>/delete', methods=['POST'])
def delete(recipe_id):
    """刪除食譜"""
    recipe = Recipe.get_by_id(recipe_id)
    if recipe and recipe.delete():
        flash("食譜已刪除", "info")
    else:
        flash("刪除失敗", "danger")
    return redirect(url_for('recipes.index'))
