FROM python:3.12-alpine

WORKDIR /app

RUN pip install fastapi fastapi-cli uvicorn

COPY main.py /app/main.py
COPY saveModel.py /app/saveModel.py
COPY data.txt /app/data.txt

CMD ["fastapi", "run", "main.py"]