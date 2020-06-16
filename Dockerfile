FROM gcr.io/google.com/cloudsdktool/cloud-sdk:latest

RUN pip --version

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

VOLUME /app
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/key-meetup.json

# docker build . -t ocr-vision
# docker create -t -i -v C:\Users\Oriol\Documents\workdir\ocr-google:/app ocr-vision /bin/bash
# docker exec -it priceless_galileo /bin/bash