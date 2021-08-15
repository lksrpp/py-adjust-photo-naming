#
# Adjust photo naming of iOS photos
#

#
# Imports
#

import os
import shutil #required?


#
# Main
#

if __name__ == "__main__":

    # source directory
    source_directory = os.path.join("..", "py-adjust-photo-naming-test")

    # storage list for filanmes to be renamed
    file_list = []

    # first run: build list of filesnames to rename later
    with os.scandir(source_directory) as dir:
        for entry in dir:
            if entry.is_file() and entry.name.endswith("_1.MOV"):
                file_list.append(entry.name[:-6] + ".HEIC")

    # second rund: rename identified files
    with os.scandir(source_directory) as dir:
        for entry in dir:
            if entry.is_file() and entry.name in file_list:
                os.rename(os.path.join(source_directory, entry.name), os.path.join(source_directory, entry.name[:-5] + "_1.HEIC"))
                print("Renamed", entry.name, "to", entry.name[:-5] + "_1.HEIC")

    
