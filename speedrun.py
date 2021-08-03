from ahk import AHK
import time
import csv
import random

coords = {}
with open('coords.csv', 'r', newline='', encoding='utf-8') as file:
	reader = csv.reader(file)
	for row in reader:
		name, coord = row
		coords[name] = tuple(map(int, coord.strip("'()").split(', ')))


# =======================Initialise and put game in focus=========================
ahk = AHK()

print(ahk.mouse_position)
win = ahk.find_window(title=b'Instagram - Google Chrome')
win.activate()


# =======================Helper funcs=========================
def click(name, delay = 5):
	if random.random()< 0.001:
		time.sleep(50*random.random())
	ahk.click(coords[name][0], coords[name][1])
	time.sleep(random.random()* delay)

def explore_profile(num_posts=10):
	click('first_post')
	for i in range(num_posts):
		click('like')
		click('next_post')
	print(f'Done exploring one profile, liked {num_posts} posts')

click('explore')
# ahk.key_down('Down')
# time.sleep(random.random()* 20)
# ahk.key_up('Down')
ahk.mouse_wheel('down',n=5)
click('explore_1')
click('userprofile')
explore_profile()