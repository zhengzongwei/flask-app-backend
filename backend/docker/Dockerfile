
# 使用官方 Python 镜像作为基础镜像
FROM python:3.12.0-slim

# 设置工作目录
WORKDIR /app

# 将本地文件拷贝到镜像中
COPY app app
COPY requirements.txt .

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装应用依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用端口
EXPOSE 5000

# 定义环境变量
ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

# 初始化数据库等操作
# 如果有初始化脚本，可以在这里执行

# 启动命令
CMD ["flask", "run"]