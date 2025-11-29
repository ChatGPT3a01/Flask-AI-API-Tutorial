# Flask AI API Tutorial

從零開始打造 AI 對話應用 - Flask + OpenAI API 完整教學

## 課程大綱

| 單元 | 主題 | 對應簡報 | 類型 |
|------|------|----------|------|
| .1 | 地端與雲端的認識 | - | 📖 概念 |
| .2 | 地端部署準備工作 | Part 1 環境準備 | 📖 概念 |
| .3 | Flask 快速入門 | Part 2 Flask 基礎實作 | 💻 實作 |
| .4 | 打造 AI 對話 API | Part 3~5 API 串接與測試 | 💻 實作 |
| .5 | 美化介面 | Part 6~7 網頁介面與串接 | 💻 實作 |
| .6 | 雲端部署準備 | Part 8 雲端部署準備 | 💻 實作 |

> **📖 概念單元**（.1、.2）為文字講解，請參考課程講義
> **💻 實作單元**（.3~.6）包含完整程式碼，收錄於本倉庫

## 簡報與程式碼對照表

| 簡報 | 內容 | 對應程式碼 |
|------|------|-----------|
| Part 1 | 環境準備（12 步驟） | 📖 概念，無程式碼 |
| Part 2 | Flask 基礎實作（6 步驟） | `.3_Flask快速入門/` |
| Part 3 | AI API 串接（4 步驟） | `.4_打造AI對話API/階段一/` |
| Part 4 | Postman 測試（4 步驟） | `.4_打造AI對話API/階段一/` |
| Part 5 | Python 腳本測試（4 步驟） | `.4_打造AI對話API/階段一/` |
| Part 6 | 網頁介面 HTML/CSS/JS（3 步驟） | `.5_美化介面/階段一/` |
| Part 7 | 前後端串接與測試（11 步驟） | `.5_美化介面/階段三/` |
| Part 8 | 雲端部署準備（5 步驟） | `.6_雲端部署準備/` |

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
