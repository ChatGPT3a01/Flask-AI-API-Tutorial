# ===========================================
# 2.5 美化介面 - 階段二：修改 Flask 應用
# 加入 render_template 提供網頁介面
# ===========================================

from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# 首頁路由：使用 render_template 提供網頁介面
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'error': '訊息不能是空的'}), 400

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "你是一個友善的 AI 助手，用繁體中文回答問題。"},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )

        ai_message = response.choices[0].message.content

        return jsonify({
            'success': True,
            'message': ai_message
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
