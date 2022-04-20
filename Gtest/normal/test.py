import cv2
from PIL import Image
from glob import glob
import os
names = glob('*.tiff')
print(names)
for name in names:
    image = cv2.imread(name)
    name_split = name.split('.')
    cv2.imwrite(name_split[0]+'.'+name_split[1]+'.png',image)
    # os.remove(name)
