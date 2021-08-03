from skimage.feature import match_template
from PIL import ImageGrab, Image
import numpy as np
import csv 
from ahk import AHK

def record_position(ahk, message = 'Please enter coord name:'):
    coordname = input(message)
    coord = ahk.mouse_position
    
    print(f'Recorded coord {coordname}, pos {coord}')
    return coord

def click(name, delay = 5):
	if random.random()< 0.001:
		time.sleep(50*random.random())
	ahk.click(coords2[name][0], coords2[name][1])
	time.sleep(random.random()* delay)

ahk = AHK()
# getting main top left...
resetter = record_position(ahk, 'Please navigate to top left of main screen and press Enter')
coords = {}
with open('coords/ipad_coords_75.csv', 'r', newline='', encoding='utf-8') as file:
	reader = csv.reader(file)
	for row in reader:
		name, coord = row
		coords[name] = tuple(map(int, coord.strip("'()").split(', ')))
normalizer = coords['main_top_left']
coords2= {}
for name, coord in coords.items():
    coords2[name] = (coord[0]-normalizer[0]+resetter[0],coord[1]-normalizer[1]+resetter[1])


like_template = Image.open('img/heart_75.png').convert('L')
template = np.array(like_template)

# do one explore post
for i in range(10):

	bbox = (coords2['explore_top_left'][0],coords2['explore_top_left'][1], coords2['explore_bot_right'][0], coords2['explore_bot_right'][1])

	im = ImageGrab.grab(bbox).convert('L')
	im.save('tmp.png')
	result = match_template(np.array(im), template, pad_input=True)
	ij = np.unravel_index(np.argmax(result), result.shape)
	keypoint = ij[:2]
	print(result.max())
	print(keypoint)


	clickpt = (coords2['explore_top_left'][0]+keypoint[1], coords2['explore_top_left'][1]+keypoint[0])
	ahk.click(clickpt)

	import time
	import random
	for i in range(3):
		ahk.click(coords2['next_post'])
		time.sleep(5*random.random())
		ahk.click(clickpt)
		time.sleep(5*random.random())
	
	click('explore_button')
	ahk.mouse_wheel('down',n=10)
	click('explore_button')
	ahk.mouse_wheel('down',n=10)
	click('explore_1')
	time.sleep(1)
