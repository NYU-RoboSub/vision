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

    # class x_center y_center x_width y_width
    temp = label[0][1]
    label[0][1] = label[0][2]
    label[0][2] = 1 - temp
    return label


def plot(images) -> None:
    # size = num of columns and rows
    size = int(sqrt(len(images)))
    # allows us to create a inch -> pixel unit
    px = 1/plt.rcParams['figure.dpi']
    # because our images are 1080 x 720 we create an image of corresponding size for all images to fit
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
        # class x_center y_center x_width y_width
        # x_center = [0, 1] -. posiiton on the image we need to multiply by dimensions
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

    # check that all data needed vor verication exists
    if not exists(f"../data/{set_id}") or not exists(f"../data/{set_id}/images") or not exists(f"../data/{set_id}/labels"):
        print(f"Set {set_id} does not exist")
        exit(1)

    # list of images in the sets img dir
    images = glob.glob(f"../data/{set_id}/images/*.jpeg")
    # list of labels in the sets label dir
    labels = glob.glob(f"../data/{set_id}/labels/*.txt")

    if len(images) != len(labels):
        print(f"Set {set_id} has {len(images)} images and {len(labels)} labels")
        exit(1)

    plot(images)

