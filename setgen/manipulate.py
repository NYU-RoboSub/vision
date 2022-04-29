import os
import sys
import glob
from PIL import Image, ImageOps, ImageFilter
import copy

def parse_label_file(file):
    # class x_center y_center width height
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
    for l in label:
        l[1] = 1 - l[1]
    
    return ["MIRROR", image.transpose(Image.FLIP_LEFT_RIGHT), label]


def save(set, name, arg):
    op, image, label = arg
    image.save(f"../data/{set}/images/{name}-{op}.jpeg")
    file = open(f"../data/{set}/labels/{name}-{op}.txt", "w")
    for l in label:
        file.write(f"{int(l[0])} {l[1]} {l[2]} {l[3]} {l[4]}\n")
    

def manipulate_set(set: str) -> None:
    # goes through all images in the set dir with extension .jpeg
    for image_path in glob.glob(f"../data/{set}/images/" + "*.jpeg"):
        # gets the image name without extension
        name = os.path.basename(image_path).replace(".jpeg", "")
        # we are getting the corresponding label file in the labels dir
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
    # going through all the images in our set dir with extension .jpeg
    for image in glob.glob(f"../data/{set}/images/*.jpeg"):
        # if the file name includes any manipulation string we delete it
        if "MIRROR" in image or "BLUR" in image or "CONTRAST" in image:
            os.remove(image)
            os.remove(image.replace("images", "labels").replace("jpeg", "txt"))


def print_usage() -> None:
    print("Usage: python manipulate.py <set_id>")


if __name__ == "__main__":
    # Check if the correct number of arguments was given
    if len(sys.argv) == 0:
        print_usage()
        exit(1)

    # assign a set id if we pass one in arguements
    set = sys.argv[1]

    # make sure that the set exists
    if not os.path.exists(f"../data/{set}"):
        print(f"Set {set} does not exist")
        exit(1)

    # clear any previous manipulations that we have done
    clear_manipulations(set)
    # this is where we actually manipulate the images
    manipulate_set(set)
