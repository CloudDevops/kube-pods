FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV POD_STATUS=Running

CMD [ "python", "./main.py" ] requirements.txt
