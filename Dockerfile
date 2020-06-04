FROM gcr.io/google.com/cloudsdktool/cloud-sdk:latest

RUN pip --version
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

VOLUME /app
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/key.json

# docker create -t -i -v C:\Users\Oriol\Documents\workdir\ocr-google:/app ocr-vision /bin/bash
