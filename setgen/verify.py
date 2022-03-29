import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import glob
from PIL import Image, ImageDraw
from math import sqrt

def parse_label(path) -> list[list[float]]:
    label = path.read().split("\n")[:-1]
    label = [x.split(" ") for x in label]
    label = [[float(y) for y in x ] for x in label]
    return label


def plot(images) -> None:
    size = int(sqrt(len(images)))
    px = 1/plt.rcParams['figure.dpi']
    _, axes = plt.subplots(nrows=size, ncols=size, sharex=True, sharey=True, figsize=((1080*size)*px, (720*size)*px))
    axes = axes.flatten()

    for img, ax in zip(images, axes):
        label_file = img.replace("images", "labels").replace(".jpeg", ".txt")

        with open(label_file, "r") as file:
            label = parse_label(file)

        label = np.array(label)
        image = Image.open(img)
        w, h = image.size
        plotted_image = ImageDraw.Draw(image)
            
        tl = np.copy(label)
        tl[:,[1,3]] = label[:,[1,3]] * w
        tl[:,[2,4]] = label[:,[2,4]] * h
        tl[:,1] = tl[:,1] - (tl[:,3] / 2)
        tl[:,2] = tl[:,2] - (tl[:,4] / 2)
        tl[:,3] = tl[:,1] + tl[:,3]
        tl[:,4] = tl[:,2] + tl[:,4]
        
        for l in tl:
            _, x0, y0, x1, y1 = l
            plotted_image.rectangle(((x0,y0), (x1,y1)), outline="red")
            
            plotted_image.text((x0, y0 - 10), "gman", fill="red")
     
        ax.imshow(np.array(image))
        ax.set_title(os.path.basename(img)[24:])
        ax.axis('off')

    plt.tight_layout()
    plt.show()


def print_usage() -> None:
    print("Usage: python verify.py <set_id>")


def exists(path: str) -> bool:
    return os.path.exists(path)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_usage()
        exit(1)

    set_id = sys.argv[1]

    if not exists(f"../data/{set_id}") or not exists(f"../data/{set_id}/images") or not exists(f"../data/{set_id}/labels"):
        print(f"Set {set_id} does not exist")
        exit(1)

    images = glob.glob(f"../data/{set_id}/images/*.jpeg")
    labels = glob.glob(f"../data/{set_id}/labels/*.txt")

    if len(images) != len(labels):
        print(f"Set {set_id} has {len(images)} images and {len(labels)} labels")
        exit(1)

    plot(images)

