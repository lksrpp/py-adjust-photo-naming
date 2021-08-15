# adjust-photo-naming
This script is used to automate the name adjustment of several hundred wrongly named photos in my personal photo library.

## Details
It looks like switching my iPhone has confused the Synology DiskStation photo backups, due to some faulty photo counter setting. As a result, there are a lot of wrongly named files that can't be correctly matched. Following some examplex to better understand the problem. Imagine two captured live photos, IMG_0001 und IMG_0002. Here is how it should look like:

1. IMG_0001.HEIC (actual photo file)
2. IMG_0001.MOV (live photo movie file)
3. IMG_0002.HEIC
4. IMG_0002.MOV

Here is how it was handled by the photo backup:

1. IMG_0001.JPG (old backup did convert HEIC files to JPG files)
2. IMG_0001.MOV (live photo move file)
3. IMG_0001.HEIC (somehow counter was wronlgy resetted and the new backup did not convert to JPG)
4. IMG_0001_1.MOV (automatically renamed to prevent duplicates, but now can't be matched by DS Photo to #3)

Target workaround:

1. IMG_0001.JPG
2. IMG_0001.MOV
3. IMG_0001_1.HEIC (add "\_1" to the file name to match with #4)
4. IMG_0001_1.MOV
