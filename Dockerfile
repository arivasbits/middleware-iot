FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY .env .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
 
EXPOSE 5000

CMD ["python", "auto_sender.py"]

