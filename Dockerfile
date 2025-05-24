FROM python:3.11-slim

LABEL authors='irfan-ahmed'

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD /bin/sh -c "python init_db.py && gunicorn --bind 0.0.0.0:5050 run:app"