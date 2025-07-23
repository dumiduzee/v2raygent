FROM python:3.14.0b4-alpine3.22

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

WORKDIR /app/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
