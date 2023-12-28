FROM python:3.11.7-slim

COPY . /var/www/src
WORKDIR /var/www/src/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python manage.py collectstatic


CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:3001", "jinbai.wsgi:application"]
