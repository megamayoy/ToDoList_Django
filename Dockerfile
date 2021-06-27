FROM python:3.7-slim-buster
RUN pip install --upgrade pip

#install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
