import cv2 as cv
import numpy as np
from PIL import Image

def replace_color_to_white(path, x, y):
    im = Image.open(path) # Can be many different formats.
    pix = im.load()
    # print(im.size)  # Get the width and hight of the image for iterating over
    # print(pix[x,y])  # Get the RGBA Value of the a pixel of an image

    # Load the aerial image and convert to HSV colourspace
    image = cv.imread(path)
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

    # Define lower and uppper limits of what we call "brown"
    delta = 0
    # color_top_left_lo = np.array([pix[x,y][0]-delta, pix[x,y][1]-delta,pix[x,y][2]-delta])
    # color_top_left_hi = np.array([pix[x,y][0]+delta, pix[x,y][1]+delta,pix[x,y][2]+delta])
    color_top_left_lo = np.array([hsv[x,y][0]-delta, hsv[x,y][1]-delta,hsv[x,y][2]-delta])
    color_top_left_hi = np.array([hsv[x,y][0]+delta, hsv[x,y][1]+delta,hsv[x,y][2]+delta])

    # Mask image to only select browns
    mask=cv.inRange(hsv,color_top_left_lo,color_top_left_hi)

    # Change image to red where we found brown
    image[mask>0]=(255,255,255)

    output_path = path[:-4] + "_white.png"
    cv.imwrite(output_path, image)
    return output_path

def concateImagesToOne(img_path_arr):
    # images = [Image.open(x) for x in ['imgs/1.png', 'imgs/8.png', 'imgs/9.png']]
    images = [Image.open(x) for x in img_path_arr]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    output_path = 'imgs/merged_white.png'
    new_im.save(output_path)
    return output_path

if __name__=="__main__":
    x = 10
    y = 10
    img_path_arr = ['imgs/1.png', 'imgs/8.png', 'imgs/9.png']
    img_output_path_arr = []
    for path in img_path_arr:
        output_path = replace_color_to_white(path, x, y)
        img_output_path_arr.append(output_path)

    output_path = concateImagesToOne(img_output_path_arr)

