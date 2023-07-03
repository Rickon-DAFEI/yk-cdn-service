# 使用基础镜像，这里以 Python 3.8 为例
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将 requirements.txt 复制到工作目录中
COPY requirements.txt .

# 安装依赖包
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 将当前目录中的所有文件复制到工作目录中
COPY . /app

# 运行应用程序
CMD ["python", "main.py"]
