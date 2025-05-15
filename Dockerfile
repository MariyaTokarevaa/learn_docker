FROM python:3.12-slim

RUN groupadd -r groupflask && useradd -r -g groupflask useradd

RUN pip install --upgrade pip

RUN pip install flask psycopg2-binary

EXPOSE 4000

WORKDIR /app

COPY . .

CMD [ "python", "site.py" ]