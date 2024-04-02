FROM python:latest
# set work directory
WORKDIR /app

ADD . /app

# install dependencies
RUN pip install -r /app/requirements.txt

CMD ["python3", "/app/main.py"]


