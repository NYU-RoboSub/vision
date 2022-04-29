from PIL import Image
import glob

for image in glob.glob("../data/curr/images/*.jpeg"):
    im = Image.open(image)
    im.resize((3024 // 4 , 4032 // 4)).save(image)


