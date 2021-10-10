# 基于 nginx:latest 镜像构建
FROM nginx:latest

# 指定信息
LABEL maintainer="test_dockerfile"

# 设置环境变量
ENV NGINX_VERSION latest
ARG workpath=/data/html/

# 切换root用户
USER root

# 执行命令，安装cur软件，设置软链接把ngin服务的日志显示到终端
RUN apt-get -yq update && apt-get install -y curl && \
ln -sf /dev/stdout /var/log/nginx/access.log && \
ln -sf /dev/stderr /var/log/nginx/error.log

# 挂载卷
VOLUME ["/data"]

# 设置工作目录
WORKDIR $workpath

# 复制 index.html 文件到nginx的html目录下
COPY index.html /usr/share/nginx/html

# 映射80端口
EXPOSE 80

# 此处CMD作为 ENTRYPOINT的参数。
CMD ["nginx","-g","daemon off;"]
# CMD ["-g","daemon off;"]
# CMD nginx -g daemon off
# 设置容器启动的命令
ENTRYPOINT ["nginx","-g","daemon off;"]

STOPSIGNAL SIGRTMAX

# 检查容器健康，通过访问 Nginx服务80端口，来判断容器服务是否健康
HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl -fs http://localhost/ || exit 1
