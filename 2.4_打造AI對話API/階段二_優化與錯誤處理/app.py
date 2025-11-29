# ===========================================
# 2.4 打造 AI 對話 API - 階段二：優化與錯誤處理
# ===========================================

from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>AI 對話應用</title>
    </head>
    <body>
        <h1>AI 對話應用（含錯誤處理）</h1>
        <p>請使用 /chat 端點進行對話</p>
    </body>
    </html>
    '''

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 步驟1：從請求中取得使用者的訊息
        data = request.json
        user_message = data.get('message', '')

        # 步驟2：驗證訊息不是空的
        if not user_message:
            return jsonify({'error': '訊息不能是空的'}), 400

        # 步驟3：呼叫 OpenAI API 取得 AI 回應
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "你是一個友善的 AI 助手，用繁體中文回答問題。"},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )

        # 步驟4：從 API 回應中提取 AI 的訊息
        ai_message = response.choices[0].message.content

        # 步驟5：將 AI 的回應以 JSON 格式回傳
        return jsonify({
            'success': True,
            'message': ai_message
        })

    except Exception as e:
        # 如果發生任何錯誤，回傳錯誤訊息
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
