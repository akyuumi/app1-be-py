FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install fastapi uvicorn
RUN pip install sqlalchemy
RUN pip install pyyaml

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]