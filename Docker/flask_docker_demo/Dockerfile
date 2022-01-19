# 基于Python开发镜像构建
FROM python:3.7.12-slim

# 指定信息
LABEL maintainer="flask_demo"

# 设置环境变量
ENV APP_VERSION latest
ARG workpath=/app

# 切换root用户
USER root

# 将工作目录切换为workpath
WORKDIR $workpath

# 将当前目录下的所有内容复制到/app目录下
ADD . /app

# pip命令安装依赖
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# 映射1234端口
EXPOSE 1234

# 设置ENTRYPOINT参数，容器进程为：python app.py
CMD ["python", "app.py"]
