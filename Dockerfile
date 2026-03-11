FROM python:3.12-slim 

COPY app/ app/
COPY requirements.txt .

RUN pip install -U -r requirements.txt

ENTRYPOINT ["fastapi", "run"]