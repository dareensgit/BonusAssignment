FROM python:3.8-slim-buster

WORKDIR /application

COPY . /application

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV APP_FILE=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
