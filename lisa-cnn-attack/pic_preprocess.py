from PIL import Image
import os

path = '../beamng_data/'
List = os.listdir(path)
for file in List:
	file_path = os.path.join(path, file)
	img = Image.open(file_path)
	if(img.mode == 'RGBA'):
		# print('******')
		img = img.convert('RGB')
	img.save(file_path)