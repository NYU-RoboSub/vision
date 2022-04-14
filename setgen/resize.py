from PIL import Image
import glob

for image in glob.glob("../data/be0564f5-8bb7-4fac-b76a-f1898b17bbda/images/*.jpeg"):
    im = Image.open(image)
    im.resize((1080, 720)).save(image)


