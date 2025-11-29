# 2.6 雲端部署準備

## 部署檔案說明

| 檔案 | 用途 |
|------|------|
| `Procfile` | 告訴雲端平台如何啟動應用 |
| `runtime.txt` | 指定 Python 版本 |
| `requirements.txt` | 套件清單（含 gunicorn） |
| `.env.example` | 環境變數範本 |
| `.gitignore` | Git 忽略清單 |

## 部署到 Render

1. 將程式碼推送到 GitHub
2. 在 Render 建立 Web Service
3. 連接 GitHub 倉庫
4. 設定環境變數（OPENAI_API_KEY）
5. 部署完成

## 部署到 Vercel

```bash
npm install -g vercel
vercel
```

## 部署到 Railway

1. 前往 railway.app
2. 連接 GitHub
3. 設定環境變數
4. 自動部署

## 本地測試生產環境

```bash
pip install gunicorn
gunicorn app:app
# 開啟 http://localhost:8000
```
