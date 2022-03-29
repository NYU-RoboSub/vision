import os
import sys
import glob
from PIL import Image, ImageOps, ImageFilter
import copy

def parse_label_file(file):
    label = file.read().split("\n")[:-1]
    label = [x.split(" ") for x in label]
    label = [[float(y) for y in x ] for x in label]
    return label

def blur(image, label, radius):
    return [f"BLUR-{radius}", image.filter(ImageFilter.GaussianBlur(radius=radius)), label]

def contrast(image, label, cutoff):
    return [f"CONTRAST-{cutoff}", ImageOps.autocontrast(image, cutoff=cutoff), label]

def mirror(image, label):
    label = copy.deepcopy(label)
    label[0][1] = 1 - label[0][1]
    return ["MIRROR", image.transpose(Image.FLIP_LEFT_RIGHT), label]

def save(set, name, arg):
    op, image, label = arg
    image.save(f"../data/{set}/images/{name}-{op}.jpeg")
    file = open(f"../data/{set}/labels/{name}-{op}.txt", "w")
    file.write(f"0 {label[0][1]} {label[0][2]} {label[0][3]} {label[0][4]}\n")
    


def manipulate_set(set: str) -> None:
    for image_path in glob.glob(f"../data/{set}/images/" + "*.jpeg"):
        name = os.path.basename(image_path).replace(".jpeg", "")
        label_path = image_path.replace("images", "labels").replace("jpeg", "txt")

        image = Image.open(image_path)
        label = parse_label_file(open(label_path, "r"))

        save(set, name, mirror(image, label))
        save(set, name, blur(image, label, 2))
        save(set, name, blur(image, label, 4))
        save(set, name, blur(image, label, 6))
        save(set, name, blur(image, label, 8))
        save(set, name, contrast(image, label, 10))
        save(set, name, contrast(image, label, 20))
        save(set, name, contrast(image, label, 30))
        save(set, name, contrast(image, label, 40))

def clear_manipulations(set: str) -> None:
    for image in glob.glob(f"../data/{set}/images/*.jpeg"):
        if "MIRROR" in image or "BLUR" in image or "CONTRAST" in image:
            os.remove(image)
            os.remove(image.replace("images", "labels").replace("jpeg", "txt"))


def print_usage() -> None:
    print("Usage: python manipulate.py <set_id>")


if __name__ == "__main__":
    if len(sys.argv) == 0:
        print_usage()
        exit(1)

    set = sys.argv[1]

    if not os.path.exists(f"../data/{set}"):
        print(f"Set {set} does not exist")
        exit(1)

    clear_manipulations(set)
    manipulate_set(set)
