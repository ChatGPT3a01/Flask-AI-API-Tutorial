# ===========================================
# API 測試腳本
# 使用方式：先啟動 Flask 應用，然後執行此腳本
# ===========================================

import requests

# 定義 API 端點網址
url = 'http://localhost:5000/chat'

# 準備要發送的訊息
data = {
    'message': '你好，請介紹一下你自己'
}

print('正在發送請求到', url)
print('訊息內容:', data['message'])
print('-' * 50)

try:
    response = requests.post(url, json=data)
    print('狀態碼:', response.status_code)
    print('回應內容:', response.json())
except requests.exceptions.ConnectionError:
    print('錯誤：無法連接到伺服器')
    print('請確認 Flask 應用已經啟動 (python app.py)')
except Exception as e:
    print('發生錯誤:', str(e))
