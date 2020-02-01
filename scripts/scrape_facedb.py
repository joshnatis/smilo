import requests

def cycle():

	site = "http://app.visgraf.impa.br/media/faces/thumbnails/s"

	for person in range(1, 38 + 1):
		for image in range(1, 3 + 1):
			prefix = ""

			if person < 10:
				prefix = "00"
			else:
				prefix = "0"

			url = site + prefix + str(person) + "/s" + prefix +  str(person) + "-0" + str(image) + "_img.jpg"
			save_images(url)

def save_images(url):
	response = requests.get(site)
	img = response.content
	with open(url[-15:], 'wb') as f:
		f.write(img)

cycle()