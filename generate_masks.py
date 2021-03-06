import os
import numpy as np
import random
from PIL import Image


def clip_bounds(n, lower, upper):
	if n < lower:
		return lower
	elif n >= upper:
		return upper - 1
	else:
		return n


def random_dir(m, x, y, iterations, padding):
	img_size = m.shape[0]

	for j in range(iterations):
		direction = random.randint(0, 3)

		if direction == 0:
			x -= padding
		elif direction == 1:
			x += padding
		elif direction == 2:
			y -= padding
		else:
			y += padding

		x = clip_bounds(x, padding, img_size - padding)
		y = clip_bounds(y, padding, img_size - padding)

		for padx in range(-padding, padding+1):
			for pady in range(-padding, padding+1):
				m[x + padx, y + pady] = 0

	return m


if __name__ == '__main__':
	image_size = 256
	num_masks = 1000
	dot_size = random.randint(1, 4)

	if not os.path.exists("mask"):
		os.makedirs("mask")

	for i in range(num_masks):
		canvas = np.ones((image_size, image_size), np.uint8)
		startx = random.randint(0, image_size-1)
		starty = random.randint(0, image_size-1)
		iterations = random.randint(5000, 10000)
		mask = random_dir(canvas, startx, starty, iterations, dot_size)

		print("iter: {:s}\n".format(str(i)))
		final_image = Image.fromarray(mask * 255).convert('1')
		final_image.save("mask/mask_{:d}.jpg".format(i))

