#
# Build FastAPI-based api with uvicorn
#

FROM python:3.9.6 

WORKDIR /usr/api

COPY . /usr/api

COPY requirements.lock .

RUN pip3 install -r requirements.lock

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]