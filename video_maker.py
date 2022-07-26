import os
import moviepy.video.io.ImageSequenceClip

image_folder='./out_images/'
file_name = "ania.mp4"
fps=90

image_files = [os.path.join(image_folder,img)
               for img in os.listdir(image_folder)
               if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(file_name)
