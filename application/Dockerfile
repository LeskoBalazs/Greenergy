FROM python:3.9-slim

RUN apt-get update
RUN apt-get install python3-pip

WORKDIR /app

COPY . /app

RUN pip install Flask gunicorn

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
