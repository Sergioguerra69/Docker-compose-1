FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app.py .
COPY templates/index.html ./templates/
COPY static/ ./static/

RUN adduser -D myuser
USER myuser

EXPOSE 5000

CMD ["python", "app.py"]