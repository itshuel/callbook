FROM python:3

RUN apt-get update && apt-get install gcc
WORKDIR /srv/web
COPY ./callbook ./srv/web
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8005

CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]
