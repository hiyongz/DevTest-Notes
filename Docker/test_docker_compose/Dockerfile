FROM python:3.7-alpine
LABEL maintainer="test_compose"

# 工作路径设定为/code
WORKDIR /code

# 创建环境变量给Flask使用
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# 复制app.py到容器内/code目录
COPY app.py /code

# 安装gcc工具、 python的依赖
RUN pip install flask && pip install redis

# 映射端口
EXPOSE 5000

STOPSIGNAL SIGTERM

# 为容器设置默认启动命令
CMD ["flask", "run"]
