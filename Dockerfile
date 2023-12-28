FROM python:3.11.7-slim

COPY . /var/www/src
WORKDIR /var/www/src/

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]
