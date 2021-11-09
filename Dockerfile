FROM python:3-alpine

ENV HTTP_PROXY="http://192.168.254.10:80"

RUN mkdir -p /home/app && pip install flask && pip install flask_limiter && pip install flask_accept

COPY . /home/app

CMD ["python", "home/app/app.py"]