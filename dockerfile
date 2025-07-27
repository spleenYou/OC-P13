FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "collectstatic", "--no-input"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
