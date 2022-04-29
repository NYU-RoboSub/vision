import glob;

def parse_label_file(file):
    # class x_center y_center width height
    label = file.read().split("\n")[:-1]
    label = [x.split(" ") for x in label]
    label = [[float(y) for y in x ] for x in label]
    return label

for label_path in glob.glob("../raw/labeled/*.txt"):
    label = parse_label_file(open(label_path, "r"))
    print(label_path)
    file = open(label_path, "w")
    for l in label:

        idx = 9999
        
        if l[0] == 16:
            idx = 2
        elif l[0] == 15:
            idx = 3
        elif l[0] == 17:
            idx = 0
        elif l[0] == 18:
            idx = 1

        file.write(f"{int(str(idx))} {l[1]} {l[2]} {l[3]} {l[4]}\n")
        
    
