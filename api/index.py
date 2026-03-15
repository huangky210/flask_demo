from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        "status": "success",
        "message": "来自 Flask 后端的问候！",
        "data": "这是通过 Vercel Serverless Function 返回的数据。"
    })

# 必须导出 app 对象供 Vercel 调用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
