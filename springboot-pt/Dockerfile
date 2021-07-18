FROM registry.cn-shanghai.aliyuncs.com/kejun/java:210718
WORKDIR /home/app
ADD target/springboot-pt.jar .
ADD bin/entrypoint.sh .
RUN chmod a+x entrypoint.sh
ENTRYPOINT ["/home/app/entrypoint.sh"]