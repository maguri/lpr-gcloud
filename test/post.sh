#!/bin/bash
echo "Convert image to base64"
echo "POST Vision API TEXT_DETECTION"
curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d @request.json https://vision.googleapis.com/v1/images:annotate # > response.json