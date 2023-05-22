# Base image
FROM python:3.8.5-slim-buster

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN useradd -ms /bin/bash user_app

RUN chown -R user_app:user_app /ticket_sales

USER user_app

WORKDIR /ticket_sales

EXPOSE 8000

CMD ["gunicorn", "ticket_sales.wsgi:application", "--bind", "0.0.0.0:8000"]
