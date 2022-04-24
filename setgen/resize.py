from PIL import Image
import glob

for image in glob.glob("../raw/*.jpg"):
    im = Image.open(image)
    im.resize((3024 // 4 , 4032 // 4)).save(image)


