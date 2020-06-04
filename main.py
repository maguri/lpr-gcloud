import io
import os
import sys

from google.cloud import vision
from src.crop     import crop
from src.vision   import get_object_plate, get_text_plate

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
print("File name: ", sys.argv[1])
file_name = os.path.abspath(sys.argv[1])
print('file: ', file_name)

plate = get_object_plate(client, file_name)

# cropped image
if plate:
  out_file_name = crop(file_name, plate.bounding_poly.normalized_vertices)
  text_plate = get_text_plate(client, out_file_name)

else:
  print('Non License Plate Found!')
  text_plate = get_text_plate(client, file_name)
  print('Text Found in image:')

print('==================')
print(text_plate)
print('==================')