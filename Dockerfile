FROM python:3.9-slim

WORKDIR /app


COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8777


ENV FLASK_APP=MainScore.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8777"]