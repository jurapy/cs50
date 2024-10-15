import os
import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

if not sys.argv[2].lower().endswith(('.jpg','.jpeg','.png')):
    sys.exit('Invalid output')

if os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit('Input and output have different extensions')

shirt_img = Image.open('shirt.png')

try:
    before_img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit('Input does not exist')
else:
    before_img = ImageOps.fit(before_img, size=(600,600))
    before_img.paste(shirt_img, mask=shirt_img)
    before_img.save(sys.argv[2])

shirt_img.close()
before_img.close()
