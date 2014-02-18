# grayscale.py
# converts color image to grayscale.
# User supplies image file path, the program opens it.
# clicking the image will change it to grayscale, then prompt user for new filename to store image
# Psuedocode for grayscale algorithm
# for each row in the image:
    # for each column in the image:
        # r, g, b = get pixel information for current row and column
        # brightness = int(round(0.299r + 0.587g + 0.114b))
        # set pixel to color_rgb(brightness, brightness, brightness)
    # update the image # to see progress row by row
import Graphics as g


def grayscale(imageName):
    win = g.GraphWin()
    image = g.Image(point(0, 0), imageName)
    # for each row in the image:
        # for each column in the image:
            # r, g, b = get pixel information for current row and column
            # brightness = int(round(0.299r + 0.587g + 0.114b))
            # set pixel to color_rgb(brightness, brightness, brightness)
        # update the image # to see progress row by row
    for row in image:
        for column in image:
            r, g, b = g.getPixel(row, column)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            g.color_rgb(brightness, brightness, brightness)

    g.draw(win)