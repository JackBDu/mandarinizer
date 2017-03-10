#!/usr/bin/env python
# encoding=utf-8

# you need to install opencv before running the script
import cv2

__author__ = "Jack B. Du"
__copyright__ = "Copyright (c) 2017, Jack B. Du"
__credits__ = ["Richard Lewei Huang", "Shirley Huang"]
__license__ = "MIT"
__email__ = "jackbdu@nyu.edu"

# REQUIRED: define the original image file here
image_file_name="sample_image.jpg"

# OPTIONAL: define the output file name here
output_file_name="mandarinized_"+image_file_name.split('.')[0]+".txt"
print image_file_name.split('.')

# OPTIONAL: define the desired resolution by image width (in pixel) here
image_width = 32

# OPTIONAL: comment out the list you like or even define your own character list
char_list = ["龘","驫","羴","掱","𣝯","淼","品","壵","尛","太","大","木","乂","人","丿","丶"] # 16-bit char list
#char_list = ["龘","驫","羴","淼","壵","从","人","一"] # 8-bit char list
#char_list = ["龘","淼","从","人"] # 4-bit char list

# OPTIONAL: whehter or not to reverse the image
image_reverse = False

# OPTIONAL: whether or not to add a space between characters
add_space = True

# open the file to write
print "loading the text file..."
file = open(output_file_name, 'w')

# read image file as grayscale
print "loading the image file..."
img = cv2.imread(image_file_name, cv2.IMREAD_GRAYSCALE)

# get the height and width of the image
height, width = img.shape

# resize the image
img = cv2.resize(img,(image_width, height*image_width/width), interpolation = cv2.INTER_CUBIC)

# get the new height and width of the image
height, width = img.shape

# loop through each row of pixels
print "converting..."

contentToWrite = ""
for i in range(height):

	# loop through each pixel in the i-th row
	for j in range(width):

		# write corresponding chinese characters based on the color of the pixel
                char_length = len(char_list)
                for k in range(char_length):
                    if img[i, j] < 256/char_length*(k+1) and img[i, j] >= 256/char_length*k:
                        if image_reverse:
                            contentToWrite += char_list[char_length-k-1]
                        else:
                            contentToWrite += char_list[k]
                        if add_space:
                            contentToWrite += ' '
                        break

	# write a new line
	contentToWrite += "\n"

print contentToWrite
file.write(contentToWrite)
# close file
file.close()
print "done!"