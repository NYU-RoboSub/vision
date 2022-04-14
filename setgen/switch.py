import os
import glob

def parse_label_file(file):
    label = file.read().split("\n")[:-1]
    print(label)
    label = [x.split(" ") for x in label]
    label = [[float(y) for y in x ] for x in label]
    return label


for label_file in glob.glob('../data/be0564f5-8bb7-4fac-b76a-f1898b17bbda/labels/*.txt'):
    print(label_file)
    with open(label_file, 'w+') as f:
        label = parse_label_file(f)
        print(label)
        #label[0][1], label[0][2] = label[0][2], 1 - label[0][1]
        #f.write(f"0 {label[0][1]} {label[0][2]} {label[0][3]} {label[0][4]}\n")



