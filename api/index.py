from flask import Flask, jsonify, send_from_directory
import os

# 初始化 Flask，并告诉它静态文件在 ../static 目录下
app = Flask(__name__, static_folder='../static')

# --- 1. 定义首页路由 ---
@app.route('/')
def index():
    # 当用户访问域名根目录时，返回 static 文件夹里的 index.html
    return send_from_directory(app.static_folder, 'index.html')

# --- 2. 现有的 API 路由 ---
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        "status": "success",
        "message": "来自 Hugging Face 后端的问候！",
        "data": "容器已成功运行。"
    })

if __name__ == '__main__':
    # 务必保持 7860 端口，这是 Hugging Face 的要求
    app.run(host='0.0.0.0', port=7860)
