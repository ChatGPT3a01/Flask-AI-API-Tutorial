# ===========================================
# 錯誤處理測試腳本
# 測試各種錯誤情況
# ===========================================

import requests

url = 'http://localhost:5000/chat'

print('=' * 50)
print('測試 1：正常訊息')
print('=' * 50)
try:
    response = requests.post(url, json={'message': '你好'})
    print('狀態碼:', response.status_code)
    print('回應:', response.json())
except Exception as e:
    print('錯誤:', e)

print()
print('=' * 50)
print('測試 2：空訊息')
print('=' * 50)
try:
    response = requests.post(url, json={'message': ''})
    print('狀態碼:', response.status_code)
    print('回應:', response.json())
except Exception as e:
    print('錯誤:', e)

print()
print('=' * 50)
print('測試 3：缺少 message 欄位')
print('=' * 50)
try:
    response = requests.post(url, json={'text': '錯誤的欄位名稱'})
    print('狀態碼:', response.status_code)
    print('回應:', response.json())
except Exception as e:
    print('錯誤:', e)
