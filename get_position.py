from ahk import AHK
import time
import csv

timestamp = time.time()
csvfile = open(f'{timestamp}_coords.csv','w')
writer = csv.writer(csvfile)

ahk = AHK()
def record_position(ahk):
    coordname = input('Type coord name: ')
    coord = ahk.mouse_position
    
    print(f'Recorded coord {coordname}, pos {coord}')
    return coord


# Constant loop.
while True:

    coordname = input('Type coord name: ')
    coord = ahk.mouse_position
    
    time.sleep(.3)
    print(f'Recorded coord {coordname}, pos {coord}')
    writer.writerow([coordname,coord])

