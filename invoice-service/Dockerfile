FROM python:3.8.3-slim-buster
RUN mkdir /invoice-service
COPY ./requirements.txt /invoice-service/requirements.txt
RUN pip install -r /invoice-service/requirements.txt
COPY . /invoice-service/
WORKDIR /invoice-service
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.main:api"]