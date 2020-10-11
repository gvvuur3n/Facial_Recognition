from PIL import Image
import numpy as np

# Code opens image, adds pixel data to npArray and saves image in BW/LA
try:
    img = Image.open("testImg.jpg").convert('LA')
    print(img.mode)
    imgWidth = img.width
    imgHeight = img.height
    imgRes = imgWidth * imgHeight

    imgArray = img.getdata()

    array = np.arange(imgRes).reshape(img.width, img.height)

    # for x in range(0, img.height-1):
    #     for y in range(0, img.width-1):
    #         array[x][y] = imgArray[x*y][0]

    print(array.shape)

    # img.save("savedImg.png")

except IOError:
    print("Error opening image")

