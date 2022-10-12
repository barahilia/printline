#!/usr/bin/env python
import cv2 as cv

from strip import make_text_spans, text_vs_blank
from builder import accords


def main():
    print('hello from hell')

    image = cv.imread('/home/iliab/proj/printline/printout.png', 0)
    image = image[200: 600, 120: 620]

    vertical_strip_images = [
        image[:, i: i + 100]
        for i in range(0, 500, 100)
    ]

    vertical_spans = [
        list(make_text_spans(text_vs_blank(vertical_strip_image)))
        for vertical_strip_image in vertical_strip_images
    ]

    for accord in accords(vertical_spans):
        print(accord)


if __name__ == '__main__':
    main()
