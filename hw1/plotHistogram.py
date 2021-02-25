"""
@author: Ketan Kokane
@description: Program that plots the histogram of an given image
"""

import cv2 # used the opencv python library to load image and convert it to numpy array
import matplotlib.pyplot as plt # use of matplotlib for plotting the result


def plot_rgb_histogram(image_name):
    """
    Function takes the name of image file and counts the RGB histogram for it
    :param image_name: path of the image to be loaded
    :return:  the function does not return anything, but creates a transformed+image_name file
    """
    img = cv2.imread(image_name) # read the image
    # Initialize 3 arrays corresponding to RGB with range from 0 t0 255
    R = [0] * 256
    G = [0] * 256
    B = [0] * 256

    for r in range(img.shape[0]): # iterate over all the row
        for c in range(img.shape[1]): # iterate over all the columns
            B[img[r][c][0]] += 1 # for every pixel get the RGB value
            G[img[r][c][1]] += 1
            R[img[r][c][2]] += 1

    plt.plot(R, color='red') #plot the histogram for color Red
    plt.plot(G, color='green') #plot the histogram for color Green
    plt.plot(B, color='blue') #plot the histogram for color Blue
    plt.title('RGB Histogram of ' + image_name)
    plt.xlabel('Pixel value from 0 to 255')
    plt.ylabel('Frequency of pixels')
    plt.savefig('RGB_Histogram.png')
    plt.show()


if __name__ == '__main__':
    plot_rgb_histogram('Lenna.png')
