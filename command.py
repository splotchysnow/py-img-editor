"""
Run linux commands, pLease run this python script through the use of a ubuntu Terminal for the commands to be recongnized.
"""
import os
from shutil import move

# all:
# 	echo "none"
# clean:
# 	rm -r ./out_images/*
# move:
# 	# Move all png files to archive
# 	mv -i ./out_images/*.png ./arc_img_out/

# redoMove:
# 	mv -i ./arc_img_out/*.png ./out_images

#a simple index shown commands.
index_command = "ls -alt"
# Junk command used to test the function
junk_command = "echo \"none\""
# the command removes everything in out_images.
clean_command = "rm -r ./out_images/*"

#move things from folder out_images to arc_image out:
move_from_img = "mv -i ./out_images/*.png ./arc_img_out/"

#move things from folder arc to out_images out:
move_to_img = "mv -i ./arc_img_out/*.png ./out_images"

# os.system(index_command)
# os.system(move_from_img)
# os.system(clean_command)

os.system("ls -alt")