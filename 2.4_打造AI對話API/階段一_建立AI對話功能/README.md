# 2.4 打造 AI 對話 API - 階段一：建立 AI 對話功能

## 學習目標
- 整合 OpenAI API 到 Flask 應用
- 建立 `/chat` API 端點
- 使用環境變數安全管理 API Key

---

## 第 1 步：安裝必要套件

在 CMD 輸入：

```bash
pip install flask openai python-dotenv requests
```

---

## 第 2 步：設定環境變數

1. 複製 `.env.example` 檔案，改名為 `.env`
2. 打開 `.env` 檔案，填入你的 API Key：

```
OPENAI_API_KEY=sk-proj-你的真實API金鑰
```

🟥 **注意**：`.env` 檔案不要上傳到 GitHub，裡面有你的密鑰！

---

## 第 3 步：啟動 API 後端

在 CMD 輸入：

```bash
python app.py
```

如果啟動成功，你會看到：

```
 * Running on http://127.0.0.1:5000
```

🟢 表示伺服器已經運作。

⚠️ **千萬不要關掉這個 CMD 視窗。**

---

## 第 4 步：開啟 Postman

下載網址：
https://www.postman.com/downloads/

安裝完成後開啟 Postman。

開啟後，你會看到一個空白工作區。

💡 如果要求登入，可以點「Skip and go to the app」跳過。

---

## 第 5 步：建立一個 POST 請求

1. 左上角按 **New**
2. 選擇 **HTTP Request**
3. 左上角的 **GET** 改為 **POST**
4. URL 輸入：

```
http://localhost:5000/chat
```

---

## 第 6 步：設定傳送的 Body（最重要）

1. 點網址下方的 **Body**
2. 選 **raw**
3. 右側選單改為 **JSON**
4. 在下面輸入：

```json
{
    "message": "你好，請介紹一下你自己"
}
```

🟢 這是一段正確的 JSON

🟥 **千萬不要**只輸入 `"message": "你好..."`

🟥 **必須**要有 `{ }` 和英文雙引號 `" "`

---

## 第 7 步：按 Send 送出 API

按下右邊的 **Send** 按鈕。

等待幾秒鐘，你會看到：

```
200 OK
```

下面會出現 JSON 回應，例如：

```json
{
    "message": "你好！我是你的 AI 助手...",
    "success": true
}
```

✅ 這代表 API 完全正常，Postman 串接成功！

---

## 常見錯誤排解

### ❌ 出現「Could not send request」
👉 請確認 Flask 應用有在執行（CMD 視窗不要關掉）

### ❌ 出現「Connection refused」
👉 請確認網址是 `http://localhost:5000/chat`，不是 `https`

### ❌ 出現 400 Bad Request
👉 請確認 Body 的 JSON 格式正確，要有 `{ }` 包起來

### ❌ 出現 500 Internal Server Error
👉 請確認 `.env` 檔案中的 `OPENAI_API_KEY` 是正確的

---

## 其他測試方式

### 使用 Python 測試腳本（最簡單）

開啟另一個 CMD 視窗，輸入：

```bash
python test_api.py
```

會自動發送測試請求並顯示結果。
