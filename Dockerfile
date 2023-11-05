FROM python:3.10.12-slim
WORKDIR django-first-app-tutorial/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]

