#!/usr/bin/env python
from argparse import ArgumentParser
import cv2 as cv

from printline.strip import make_text_spans, text_vs_blank
from printline.builder import accords


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('image')
    return parser.parse_args()


def main():
    args = parse_args()

    image = cv.imread(args.image, 0)
    image = image[200: 600, 120: 620]

    vertical_strip_images = [
        image[:, i: i + 50]
        for i in range(0, 500, 50)
    ]

    vertical_spans = [
        list(make_text_spans(text_vs_blank(vertical_strip_image)))
        for vertical_strip_image in vertical_strip_images
    ]

    for span in vertical_spans:
        print(span)

    out = cv.merge((image, image, image))
    color = 255, 0, 0
    thickness = 2

    print('Accords')

    for accord in accords(vertical_spans):
        print(accord, end=' - ')

        start, end = accord

        p1 = 5, start
        p2 = 495, end
        out = cv.rectangle(out, p1, p2, color, thickness)

    print()
    cv.imwrite('out.png', out)


if __name__ == '__main__':
    main()
