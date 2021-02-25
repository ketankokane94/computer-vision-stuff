"""
@Author : Kokane Ketan
@Description: Main program which reads an image and converts it to XYZ format and prints its RGB histogram
"""
from plotHistogram import plot_rgb_histogram
from convertRGBToCIE import convertToCIE

def main():
    convertToCIE('Lenna.png')
    plot_rgb_histogram('Lenna.png')

if __name__ == '__main__':
    main()
