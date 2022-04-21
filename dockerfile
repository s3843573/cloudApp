FROM python:3.7

RUN apt-get update && apt-get install

WORKDIR /code
# COPY requirements.txt /code/
COPY . /code/
RUN pip install -r requirements.txt && python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]