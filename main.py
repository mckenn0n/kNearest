
import sys
import os
import numpy as np
import matplotlib.pyplot as mplot
from PIL import Image

# ((a[0]-b[0])**2)+((a[1]-b[1])**2)
def change(k,ref_image, point_map, i, j):
	red = 0
	green = 0
	blue = 0
	dist_list = []
	new_map = {}
	for ref_key in point_map:
		new_map[ref_key] = ((ref_key[0]-(i,j)[0])**2)+((ref_key[1]-(i,j)[1])**2)
	dist_list = sorted(new_map, key=new_map.get, reverse = False)
	for key in range(k):
		red += ref_image[dist_list[key][0]][dist_list[key][1]][0]
		blue += ref_image[dist_list[key][0]][dist_list[key][1]][2]
		green += ref_image[dist_list[key][0]][dist_list[key][1]][1]
	return [round(red/k), round(green/k), round(blue/k), 255]



def main():
	args = sys.argv

	if len(args)!=3:
		print("Wrong number of of command lind arguments")
		sys.exit()

	k = int(args[1])
	point_map = {}
	file_name = args[2]
	ref_image = Image.open(file_name)
	change_image = Image.open("us_outline.png")
	ref_image = np.uint8(ref_image)
	change_image = np.uint8(change_image)
	change_image.flags.writeable = True

	for i, row in enumerate(ref_image):
		for j, pixel in enumerate(row):
			if (ref_image[i][j][0] != 0) or (ref_image[i][j][1] != 255) or (ref_image[i][j][2] != 0):
				point_map[(i,j)] = ref_image[i][j]

	for i, row in enumerate(change_image):
		for j, pixel in enumerate(row):
			if (change_image[i][j][0] == 0) and (change_image[i][j][1] == 255) and (change_image[i][j][2] == 0):
				change_image[i][j] = change(k, ref_image, point_map, i, j)
	Image.fromarray(change_image)
	mplot.imshow(change_image)
	mplot.show()





if __name__ == "__main__":
    main()
