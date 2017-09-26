FROM python:3.6-stretch
WORKDIR /app
ADD . /app
VOLUME /data
ENV CHITCHAT_MODEL /data
RUN pip install -r requirements.txt
CMD ["nameko", "run", "--config", "./config.yaml", "service:ChitChat"]