FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/staticfiles

ARG SENTRY_DSN=""
ARG SECRET_KEY="dummy-key-for-build"
ARG SERVER_TYPE="DEV"
ARG HOSTS="localhost"

ENV SENTRY_DSN=$SENTRY_DSN
ENV SECRET_KEY=$SECRET_KEY
ENV SERVER_TYPE=$SERVER_TYPE
ENV HOSTS=$HOSTS

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
