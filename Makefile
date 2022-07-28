all:
	echo "none"
clean:
	rm -r ./out_images/*
move:
	# Move all png files to archive
	mv -i ./out_images/*.png ./arc_img_out/

redoMove:
	mv -i ./arc_img_out/*.png ./out_images