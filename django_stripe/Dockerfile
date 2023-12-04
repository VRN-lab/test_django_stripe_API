FROM python:3.10

ENV SECRET_KEY=${SECRET_KEY}
ENV SECRET_KEY_STRIPE=${SECRET_KEY_STRIPE}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/