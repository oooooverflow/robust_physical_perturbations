import cv2
import os

path = 'beamng_data/'
List = os.listdir(path)

save_path = 'beamng_resize32'

crop_size = (32, 32)
for file in List:
	file_path = os.path.join(path, file)
	img = cv2.imread(file_path)
	img_new = cv2.resize(img, crop_size, interpolation = cv2.INTER_CUBIC)
	new_path = os.path.join(save_path, file)
	cv2.imwrite(new_path, img_new)