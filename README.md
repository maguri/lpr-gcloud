# lpr-gcloud


LPR with Google Cloud Vision AI with [Python Client Library](https://cloud.google.com/vision/docs/libraries#client-libraries-install-python).

This is a simple lib to use Google  Cloud to read Licens Plate numbers.

![image](https://user-images.githubusercontent.com/14354821/127286974-9b9e5f07-3d3e-4c69-8dfe-2e78f021e2e1.png)
## How it works
The script find the object "Licens Plate", crop the plate, and detect the plate text.
## Getting Started

**Google Console Account**. Create a service account and download the private key file
Read the docs: https://cloud.google.com/vision/docs/setup

**Docker**. This is an image from [gcr.io/google.com/cloudsdktool/cloud-sdk:latest](https://github.com/GoogleCloudPlatform/cloud-sdk-docker)
```
docker build . -t lpr-gcloud
docker create -t -i -v /Path/To/Your/Repo:/app -t lpr-gcloud /bin/bash
```
Run or exec the script into the container
```
docker exec -it tender_dirac python3.7 main.py image/linux/format/path/file.jpg
```

## Tools
- Python 3.7
- google-cloud-vision 1.0.0
- Pillow 7.1.2

## TODO
- [ ] Crop Until Find License Plate Object

## LICENSE
MIT
