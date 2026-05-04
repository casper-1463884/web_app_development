# 智慧烹飪菜單系統 - 路由設計文件 (Routes)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁儀表板** | GET | `/` | `index.html` | 顯示今日菜單摘要與庫存提醒 |
| **食譜列表** | GET | `/recipes` | `recipes/index.html` | 瀏覽與搜尋所有食譜 |
| **食譜詳情** | GET | `/recipes/<id>` | `recipes/detail.html` | 顯示步驟、食材與營養資訊 |
| **新增食譜頁面** | GET | `/recipes/new` | `recipes/new.html` | 填寫新食譜表單 |
| **建立食譜** | POST | `/recipes` | — | 接收表單並存入資料庫 |
| **編輯食譜頁面** | GET | `/recipes/<id>/edit` | `recipes/edit.html` | 顯示編輯表單 |
| **更新食譜** | POST | `/recipes/<id>/update` | — | 更新食譜資料 |
| **刪除食譜** | POST | `/recipes/<id>/delete` | — | 刪除食譜後重導向至列表 |
| **每週菜單規劃** | GET | `/menu` | `menu/index.html` | 顯示每週菜單視圖 |
| **新增至菜單** | POST | `/menu/add` | — | 將食譜排入特定日期與餐次 |
| **從菜單移除** | POST | `/menu/<id>/delete` | — | 移除某天的特定餐次 |
| **食材庫存管理** | GET | `/pantry` | `pantry/index.html` | 顯示目前所有食材庫存 |
| **新增/更新庫存** | POST | `/pantry/update` | — | 批次更新庫存數量或新增食材 |
| **智慧推薦 API** | GET | `/api/recommend` | — | 根據庫存回傳推薦食譜 (JSON) |
| **購物清單** | GET | `/shopping-list` | `shopping_list.html` | 顯示自動生成的採買清單 |

---

## 2. 每個路由的詳細說明

### 食譜管理 (Recipes)
- **新增食譜 (POST /recipes)**
  - **輸入**：`title`, `description`, `instructions`, `ingredients` (列表), `servings`.
  - **邏輯**：建立 Recipe 物件，並在 `recipe_ingredients` 關聯食材。
  - **輸出**：重導向至 `/recipes/<id>`。
- **編輯食譜 (POST /recipes/<id>/update)**
  - **輸入**：同上。
  - **邏輯**：更新 Recipe 物件，同步更新關聯的 `recipe_ingredients`。

### 菜單規劃 (Menu)
- **新增至菜單 (POST /menu/add)**
  - **輸入**：`recipe_id`, `date`, `meal_type`.
  - **邏輯**：建立 `MenuPlan` 紀錄。
  - **輸出**：重導向至 `/menu`。

### 食材庫存 (Pantry)
- **更新庫存 (POST /pantry/update)**
  - **輸入**：`item_id`, `new_quantity`, `expiry_date`.
  - **邏輯**：更新 `Pantry` 紀錄。

---

## 3. Jinja2 模板清單

所有模板皆繼承自 `templates/base.html`。

- `base.html`：包含導覽列、頁尾與 CSS/JS 引用。
- `index.html`：系統概況。
- `recipes/index.html`：食譜卡片列表。
- `recipes/detail.html`：清爽的步驟展示頁面。
- `recipes/new.html` / `edit.html`：包含動態增減食材欄位的表單。
- `menu/index.html`：日曆風格的規劃表。
- `pantry/index.html`：條列式的食材清單。
- `shopping_list.html`：可勾選的待買清單。

---

## 4. 路由骨架說明

對應的程式碼骨架已建立於 `app/routes/` 目錄下。
