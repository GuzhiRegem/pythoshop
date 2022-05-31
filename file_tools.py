#!/usr/bin/python3
"""
    module
"""
import numpy as np
from PIL import Image

def open_image(name):
    img = Image.open(name)
    tmp = np.array(img)
    out = np.ndarray(shape=tmp.shape)
    for x in range(tmp.shape[0]):
        for y in range(tmp.shape[1]):
            out[tmp.shape[0] - x - 1, y] = tmp[x, y]
    return out.astype(np.uint8)

def save_image(array, name):
    tmp = array
    out = np.ndarray(shape=tmp.shape)
    for x in range(tmp.shape[0]):
        for y in range(tmp.shape[1]):
            out[tmp.shape[0] - x - 1, y] = tmp[x, y]
    img = Image.fromarray(out.astype(np.uint8))
    img.save(name)

