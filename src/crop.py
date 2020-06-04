from PIL import Image

def crop(image_file, vectors):
	image = Image.open(image_file)
	print(image)
	width, height = image.size

	left 	 = vectors[3].x * width
	top  	 = vectors[3].y * height
	right  = vectors[1].x * width
	bottom = vectors[1].y * height

	print(vectors)

	image_cropped = image.crop((left, bottom, right, top))
	# image_cropped = image.crop((10, 100, 150, 200))
	image_cropped.save('test_img/out.jpg')

	return 'test_img/out.jpg'