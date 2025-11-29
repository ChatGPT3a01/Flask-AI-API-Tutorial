# 2.3 Flask 快速入門

## 學習目標
- 認識 Flask 框架的核心概念
- 建立第一個 Flask 應用
- 理解路由（Route）和視圖函數（View Function）

## 執行方式

```bash
# 1. 啟動虛擬環境
cd AI_Projects
venv\Scripts\activate  # Windows

# 2. 安裝 Flask（如果還沒安裝）
pip install flask

# 3. 進入此資料夾
cd 2.3_Flask快速入門

# 4. 執行應用
python app.py
```

## 測試

開啟瀏覽器：
- http://localhost:5000/ → 首頁
- http://localhost:5000/hello → Hello 頁面

## 檔案說明

| 檔案 | 說明 |
|------|------|
| app.py | Flask 主程式，包含兩個路由 `/` 和 `/hello` |
