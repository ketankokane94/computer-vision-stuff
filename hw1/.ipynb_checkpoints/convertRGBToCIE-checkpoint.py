"""
@Author : Kokane Ketan
@Description: Program which converts the image from RGB color space to CIE-XYZ color space
"""

import cv2


def convertToCIE(image_name):
    """
    Function which converts the image from RGB to CIE- XYZ color space
    :param image_name: path of the file name to be converted
    :return:  the function does not return anything but prints and saves the file
    """
    img = cv2.imread(image_name) # load the file using Cv2 library
    cie = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ) # using cvtColor function to change the color space from RGB to CIE XYZ
    cv2.imshow('Transformed_CIE'+image_name, cie) # showing the
    cv2.imwrite('Transformed_CIE'+image_name, cie)
    cv2.waitKey(0)


if __name__ == '__main__':
    convertToCIE('Lenna.png')
