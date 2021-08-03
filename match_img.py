from skimage.feature import match_template
from PIL import ImageGrab, Image
import numpy as np
import csv 

coords = {}
with open('ipad_coords_75.csv', 'r', newline='', encoding='utf-8') as file:
	reader = csv.reader(file)
	for row in reader:
		name, coord = row
		coords[name] = tuple(map(int, coord.strip("'()").split(', ')))


like_template = Image.open('heart.png').convert('L')
template = np.array(like_template)

bbox = (coords['explore_top_left'][0],coords['explore_top_left'][1], coords['explore_bot_right'][0], coords['explore_bot_right'][1])


im = ImageGrab.grab(bbox)
im.save('tmp.png')
result = match_template(np.array(im), template, pad_input=True)
ij = np.unravel_index(np.argmax(result), result.shape)
keypoint = ij[:-1]
print(result.max())
print(keypoint)