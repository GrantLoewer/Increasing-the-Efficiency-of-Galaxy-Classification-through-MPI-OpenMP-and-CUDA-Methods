import subprocess
import glob
import os
import time

starting_folders = ["original_images","finished"]
images_folder = "original_images"
finished_folder = "finished"

for folder in starting_folders:
    if (os.path.isdir(folder) == True):
        pass
    else:
        os.mkdir(folder)
        print("Creating '{}' folder.".format(folder))

for filename in os.listdir('./'):
    if filename.endswith('.tif'):
        image = filename
        print("Starting {}".format(image))
        print("at {}".format(time.asctime()))
        image_no_file_extension = os.path.splitext(image)[-0]
        os.mkdir('./{}/{}'.format(finished_folder, image_no_file_extension))
        x = 0
        while x <= 111:
            y = 0
            while y <= 111:
                command_tile = 'convert -quiet -define tif:size=120x120 {}[9x9+{}+{}] "./{}/{}/{} {}x{}.tif"'.format(image, x, y, finished_folder, image_no_file_extension, image_no_file_extension, x, y) #/dev/null from linux
                os.system(command_tile)
                y = y + 1
            x = x + 1
        print("Finished {}".format(image))
        print("at {}".format(time.asctime()))
        os.rename(image, './{}/{}'.format(images_folder, image))
    else:
        pass
