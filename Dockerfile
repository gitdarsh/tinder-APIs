FROM python:3.11-slim

WORKDIR /tinder

COPY ./requirements.txt /tinder/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /tinder/

CMD ["uvicorn", "app.server:tinder", "--host", "0.0.0.0", "--port", "8080", "--reload"]
