import numpy as np
from matplotlib import pyplot as plt
from glob import glob

def create_heatmap(path_to_annotations, width, height):
    heatmap = np.zeros((height, width))
    pathes = glob(path_to_annotations + '//*')

    for pth in pathes:
        with open(pth, 'r') as f:
            for line in f:
                x, y, w, h = map(float, line.split(' ')[-4:])
                x_center = int(x * width)
                y_center = int(y * height)
                w = int(w * width)
                h = int(h * height)
                x1 = int(x_center - w / 2)
                y1 = int(y_center - h / 2)
                x2 = x1 + w
                y2 = y1 + h
                heatmap[y1:y2, x1:x2] += 1
    return heatmap

def show_heatmap(path_to_annotations, width, height):
    hmap = create_heatmap(path_to_annotations, width, height)
    plt.imshow(hmap, cmap='afmhot')
    plt.show()
