import sys  # For args in commandline when runnign the script
import os # For filepaths, and files list
from PIL import Image # Principal libreary for image maniupulation

# When running file from command line we will pass the following arguments:
folder_name = sys.argv[1] # path where we have the images
new_folder_name = sys.argv[2] # new folder we are creating to save images

if not os.path.exists(new_folder_name):
    os.mkdir(new_folder_name) # pretty straight forward. If our new folder doesnt exist, we cereate it, if no, just continue

for file in os.listdir(folder_name): # we make a list of the different files in our folder
    img = Image.open(f'./{folder_name}/{file}') # We open each image
    clean_name = os.path.splitext(file) # we divide the file name, from the main name AND their extension. EX: ('image', 'jpg')
    img.save(f'./{new_folder_name}/{clean_name[0]}.png', 'png') # We save the image on the new folder, with their new extension and converted to PNG
    