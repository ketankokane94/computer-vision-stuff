"""
@author: Ketan Kokane
@description: Code to apply linear filter on data

"""

import numpy as np
import cv2


def get_filter():
    """
    Initialize a 3,3 numpy array with the given values
    :return: a numpy array with kernel
    """
    return np.array([-2, 3, -1, 4, -1, 2, 0, 5, 3]).reshape(3, 3)


def element_wise_product(a, b):
    """
    Perform element-wise multiplication of two numpy arrays
    :param a: np array 1
    :param b: np array 2
    :return: sum of element wise multiplication of a and b
    """
    return np.sum(a * b)


def convolve(img, pad_img, kernel):
    """

    :param img: img in numpy array
    :param pad_img: padded image
    :param kernel:
    :return: convolved image with kernel values of same shape as img
    """
    result = np.zeros((img.shape[0], img.shape[1]))
    img_top_left = 0
    kernel_bottom_right = kernel.shape[1]
    for row in range(0, img.shape[1]):
        for col in range(0, img.shape[1]):
            slices_img = pad_img[img_top_left + row: kernel_bottom_right + row,
                         img_top_left + col:kernel_bottom_right + col]
            result[row][col] = element_wise_product(slices_img, kernel)
    return result


def Q2():
    """
    Code to solve the Question 2 of the homework
    :return:
    """
    img = np.array(
        [10, 8, -2, 0, 1, 6, 3, 5, 3, 2, -4, 11, 7, -1, 7, 1]).reshape(4, 4)
    kernel = get_filter()  # get the filter to use
    pad_img = np.pad(img, 1, mode='edge')  # pad the data to bleed the eges
    resultant_img = convolve(img, pad_img, kernel)  # perform element-wise
    # multiplication
    print('Resultant Image')
    print(resultant_img)  # print the resultant image


def scale_image(resultant_img):
    """
    Routine to scale the resultant image to make the sure the values are
    between 0 to 255
    :param resultant_img: 2-D numpy array
    :return: scaled numpy array
    """
    max = np.max(resultant_img)  # get the maximum value of the resultant image
    scaling_factor = max / 255  # find a number required to scale the maximum
    # value in the array to make it equal to 255
    resultant_img = resultant_img / scaling_factor
    resultant_img = resultant_img.astype(np.uint8)  #  cv2 works with
    # unsigned integers to convert the resultant image to that
    return resultant_img


def Q3():
    """
    routine to contain code for Question 3
    :return:
    """
    img = cv2.imread('Lenna.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #  convert the BGR image to
    # grayscale
    kernel = get_filter()
    pad_img = np.pad(img, 1, mode='edge')
    resultant_img = convolve(img, pad_img, kernel)
    resultant_img = scale_image(resultant_img)
    print('Image displayed, press any key to quit!')
    cv2.imwrite('Transformed_Lenna.png', resultant_img)
    cv2.imshow('Transformed Image', resultant_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# run only if not executed as a script
if __name__ == '__main__':
    Q2()
    Q3()
