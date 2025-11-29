# Flask AI API Tutorial

從零開始打造 AI 對話應用 - Flask + OpenAI API 完整教學

## 課程大綱

| 單元 | 主題 | 說明 | 類型 |
|------|------|------|------|
| .1 | 地端與雲端的認識 | 兩種部署方式的概念與選擇策略 | 📖 概念 |
| .2 | 地端部署準備工作 | Python 環境確認、虛擬環境建立 | 📖 概念 |
| .3 | Flask 快速入門 | Python Web 框架基礎 | 💻 實作 |
| .4 | 打造 AI 對話 API | 串接 OpenAI API，建立對話功能 | 💻 實作 |
| .5 | 美化介面 | 前端 HTML/CSS/JS 整合 | 💻 實作 |
| .6 | 雲端部署準備 | Heroku / Render 部署設定 | 💻 實作 |

> **📖 概念單元**（.1、.2）為文字講解，請參考課程講義
> **💻 實作單元**（.3~.6）包含完整程式碼，收錄於本倉庫

## 目錄結構

```
Flask-AI-API-Tutorial/
├── .3_Flask快速入門/
│   ├── app.py              # 基礎 Flask 應用
│   └── README.md
├── .4_打造AI對話API/
│   ├── 階段一_建立AI對話功能/
│   └── 階段二_優化與錯誤處理/
├── .5_美化介面/
│   ├── 階段一_HTML介面結構/
│   ├── 階段二_修改Flask應用/
│   └── 階段三_測試與除錯/
├── .6_雲端部署準備/
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   └── runtime.txt
└── 簡報/                    # 教學簡報 (HTML)
```

## 快速開始

### 1. 環境準備

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (Windows)
venv\Scripts\activate

# 啟動虛擬環境 (Mac/Linux)
source venv/bin/activate

# 安裝套件
pip install flask openai python-dotenv
```

### 2. 設定 API Key

```bash
# 複製範例檔案
copy .env.example .env

# 編輯 .env 檔案，填入你的 OpenAI API Key
OPENAI_API_KEY=your-api-key-here
```

### 3. 執行應用

```bash
python app.py
```

開啟瀏覽器前往 http://localhost:5000

## 技術棧

- **後端**: Python, Flask
- **AI**: OpenAI API (GPT-4)
- **前端**: HTML, CSS, JavaScript
- **部署**: Heroku / Render

## 簡報

`簡報/` 資料夾包含完整教學簡報：

- Part1 - 環境準備
- Part2 - Flask 基礎實作
- Part3 - AI API 串接
- Part4 - Postman 測試
- Part5 - Python 腳本測試
- Part6 - 網頁介面
- Part7 - 前後端串接
- Part8 - 雲端部署準備

開啟 `簡報/index.html` 即可瀏覽所有簡報。

## 授權

MIT License
