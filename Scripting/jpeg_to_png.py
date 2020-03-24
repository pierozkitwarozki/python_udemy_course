from PIL import Image
import os
import sys

directory = str(sys.argv[1])  # first arg - dir with jpeg files
save_dir = str(sys.argv[2])  # second arg - dir with png files

if not os.path.exists(save_dir): # if saving dir does not exist, create it
    os.mkdir(save_dir)

if os.path.isdir(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            clean_name = os.path.splitext(filename)[0]  # getting file name
            img = Image.open(os.path.join(directory, filename))
            img.save(f'{save_dir}/{clean_name}.png', 'png')
            continue
        else:
            continue
else:
    print('No such directory')
