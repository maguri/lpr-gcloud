# Imports the Google Cloud client library
import io
import os

from google.cloud.vision import types

OBJECT_ID = 'License plate'

def get_object_plate(client, file_name):
	plate = None
	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	print('imagefile: ', image_file)
	image = types.Image(content=content)

	# Performs object detection on the image file
	objects = client.object_localization(image=image).localized_object_annotations
	print('Number of objects found: {}'.format(len(objects)))

	for object_ in objects:
		if (object_.name == OBJECT_ID):
		  # print('\n{} (confidence: {})'.format(object_.name, object_.score))
		  # print('Normalized bounding polygon vertices: ')
		  plate = object_
		  print('Found:', plate)
		  print(object_.bounding_poly.normalized_vertices)

		  for vertex in object_.bounding_poly.normalized_vertices:
		    print(' - ({}, {})'.format(vertex.x, vertex.y))

	if (not plate):
		print('Not Found')

	return plate

def get_text_plate(client, file_name):
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)

	# Performs object detection on the image file
	response = client.text_detection(image=image)
	texts = response.text_annotations
	print('Text detected: {}'.format(len(texts)))
	plate = texts[0].description
	print('license plate:', plate)

	for text in texts:
		print('text: "{}"'.format(text.description))

		vertices = (['({},{})'.format(vertex.x, vertex.y)
									for vertex in text.bounding_poly.vertices])

	print('bounds: {}'.format(','.join(vertices)))

	return plate