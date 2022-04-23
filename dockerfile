FROM python:3.7

RUN apt-get update && apt-get install

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt && python manage.py migrate
RUN python manage.py collectstatic --noinput
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=cloudApp.production"]