FROM python:3-alpine

ADD src/ app/
WORKDIR /app

RUN pip install -r requirements.txt


EXPOSE 3000
CMD ["python", "app.py"]