import numpy as np
import matplotlib.pyplot as plt
import random
import os
from PIL import Image, ImageDraw

images = [os.path.join('./data/0.1/images', x) for x in os.listdir('data/0.1/images')]
annotations = [os.path.join('./data/0.1/labels', x) for x in os.listdir('./data/0.1/labels') if x[-3:] == "txt"]

def plot_bounding_box(image, annotation_list):
    annotations = np.array(annotation_list)
    w, h = image.size
    
    plotted_image = ImageDraw.Draw(image)

    transformed_annotations = np.copy(annotations)
    transformed_annotations[:,[1,3]] = annotations[:,[1,3]] * w
    transformed_annotations[:,[2,4]] = annotations[:,[2,4]] * h 
    
    transformed_annotations[:,1] = transformed_annotations[:,1] - (transformed_annotations[:,3] / 2)
    transformed_annotations[:,2] = transformed_annotations[:,2] - (transformed_annotations[:,4] / 2)
    transformed_annotations[:,3] = transformed_annotations[:,1] + transformed_annotations[:,3]
    transformed_annotations[:,4] = transformed_annotations[:,2] + transformed_annotations[:,4]
    
    for ann in transformed_annotations:
        obj_cls, x0, y0, x1, y1 = ann
        plotted_image.rectangle(((x0,y0), (x1,y1)))
        
        plotted_image.text((x0, y0 - 10), "gman")
    
    plt.imshow(np.array(image))
    plt.show()


def parse_annotation_file(file):
    annotation_list = file.read().split("\n")[:-1]
    annotation_list = [x.split(" ") for x in annotation_list]
    annotation_list = [[float(y) for y in x ] for x in annotation_list]

    return annotation_list

annotation_file = random.choice(annotations)
with open(annotation_file, "r") as file:
    annotation_list = parse_annotation_file(file)

print(annotation_file)
image_file = annotation_file.replace("labels", "images").replace("txt", "jpeg")
assert os.path.exists(image_file)


image = Image.open(image_file)

print(annotation_list)
print(image_file)

plot_bounding_box(image, annotation_list)
