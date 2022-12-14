#!/usr/bin/env python
from argparse import ArgumentParser
import cv2 as cv

from printline.strip import make_text_spans, text_vs_blank
from printline.builder import accords, comp_nearby_tuples


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('image')
    parser.add_argument('-w', '--width', type=int, default=50)
    return parser.parse_args()


def main():
    args = parse_args()

    image = cv.imread(args.image, 0)
    height, width = image.shape

    vertical_strip_images = [
        image[:, i: i + args.width]
        for i in range(0, width, args.width)
    ]

    vertical_spans = [
        list(make_text_spans(text_vs_blank(vertical_strip_image)))
        for vertical_strip_image in vertical_strip_images
    ]

    for span in vertical_spans:
        print(span[: 3])

    out = cv.merge((image, image, image))
    color = 255, 0, 0
    thickness = 2

    print()
    print('Accords')

    res = accords(vertical_spans, comp=comp_nearby_tuples(6), same_ratio=0.25)

    for accord in res:
        print(accord, end=' - ')

        start, end = accord

        p1 = 5, start
        p2 = width - 5, end
        out = cv.rectangle(out, p1, p2, color, thickness)

    print()
    cv.imwrite('out.png', out)


if __name__ == '__main__':
    main()
