# 使用轻量级 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有项目文件
COPY . .

# 暴露端口 (HF 默认 7860)
EXPOSE 7860

# 启动 Flask
CMD ["python", "api/index.py"]
