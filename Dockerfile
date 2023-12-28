FROM python:3.11.7-slim

COPY . /var/www/src
WORKDIR /var/www/src/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["python", "manage.py", "runserver", "0:8000"]
