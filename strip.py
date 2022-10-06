import numpy as np


def black_white_filter(arr, threshold=240):
    res = np.array(arr)

    res[res < threshold] = 0
    res[res > 0] = 1

    return res


def text_vs_blank(bw):
    horizontal_whites = np.sum(bw, axis=1)

    threshold = 0.9 * np.max(horizontal_whites)
    mask = horizontal_whites < threshold

    text_blank = np.ones_like(horizontal_whites)
    text_blank[mask] = 0

    return text_blank


def make_text_spans(it):
    it = iter(it)
    prev = next(it)
    start = 0

    for i, value in enumerate(it):
        if prev != value:
            if prev == 0:
                yield start, i
            else:  # prev == 1
                start = i
        prev = value

    if prev == 0:
        yield start, i


def mark_text(im, text_spans):
    import cv2 as cv

    height, width = im.shape

    three_colors = im, im, im
    out = cv.merge(three_colors)

    red = 255, 0, 0
    thickness = 1

    for start, end in text_spans:
        p1 = 5, start
        p2 = width - 5, end
        out = cv.rectangle(out, p1, p2, red, thickness)

    return out
