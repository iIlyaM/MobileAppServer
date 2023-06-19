#
FROM python:3.10

#
WORKDIR /app
COPY ./app .
#
COPY requirements.txt .

#
RUN pip3 install -r requirements.txt
#

#
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
