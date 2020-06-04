# lpr-gcloud
LPR with Google Cloud Vision AI with [Python Client Library](https://cloud.google.com/vision/docs/libraries#client-libraries-install-python).

This is a simple lib to use Google  Cloud to read Licens Plate numbers.

## How it works
The script find the object "Licens Plate", crop the plate, and detect the plate text.
## Getting Started

**Google Console Account**. Create a service account and download the private key file
Read the docs: https://cloud.google.com/vision/docs/setup

**Docker**. This is an image from [gcr.io/google.com/cloudsdktool/cloud-sdk:latest](https://github.com/GoogleCloudPlatform/cloud-sdk-docker)
```
docker create -t -i -v /Path/To/Your/Repo:/app -t lpr-gcloud /bin/bash
```
Run or exec the script into the container
```
python3.7 main.py image/file
```

## Tools
- Python 3.7
- google-cloud-vision 1.0.0
- Pillow 7.1.2

## TODO
- [ ] Crop Until Find License Plate Object

## LICENSE
MIT
