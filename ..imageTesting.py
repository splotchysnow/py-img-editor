"""
This file purpose is to test all my functions that are written in other libraries.
Author: Guan Li
"""
from gray_scale_functions import *
from inversion import *
#Load Images
img = loadImg("./img/wired_cat.webp")

# ------------- Test for the Gray Scale functions: -------------------------
# # Normal Scaling Color test
# lightScale(img,"gs_light_scale.png")
# darkScale(img,"gs_dark_scale.png")
# avgScale(img,"gs_avg_scale.png")
# # Light Scale Color Test
# lightScale_Blue(img,"gsl_blue.png")
# lightScale_Green(img,"gsl_green.png")
# lightScale_Red(img,"gsl_red.png")
# lightScale_Cyan(img,"gsl_cyan.png")
# lightScale_Pink(img,"gsl_pink.png")
# lightScale_Yellow(img,"gsl_yellow.png")
# # Dark Scale Color Test
# lightScale_Blue(img,"gsd_blue.png")
# lightScale_Green(img,"gsd_green.png")
# lightScale_Red(img,"gsd_red.png")
# lightScale_Cyan(img,"gsd_cyan.png")
# lightScale_Pink(img,"gsd_pink.png")
# lightScale_Yellow(img,"gsd_yellow.png")
# avgImprovedScale(img, "imp.png")

# ----------------------- End of test -------------------------------------------


# ----------------------- Test for edge Detection --------------------------------
# Edge_Detection_Function(loadImg("./img/wired_cat.webp"), "cat_edge_detection.png", 70)

# ----------------------- Test for downSize --------------------------------------


# ----------------------- Test for select Pixels -------------------------------
 #img = loadImg("./img/caokitten.jpg")
 #select_pixels(img,"EditedKitty")

# ----------------------- Test for flip/rotate -----------------------------------------
# flip_image_up_and_down(img,"flipedCat")
# flip_image_left_and_right(img,"LRflippedCat")
# img = half_reversion_bonus_LR(img,"weirdLeft/R Flip")
# img = half_reversion_bonus_UD(img,"cat double flip")
# img = lightScale_Red(img, "Flipped and pinked")
# img = down_size_image(img, "redFlippedDownsized",2)
# img = Edge_Detection_Function(img, "edgeAfterFlip", 3)
# Testing rotation:


# It works since rotate 4 times kept the same img
# img = rotation_right(img, "rotate_right")
# img = rotation_right(img, "rotate_right")
# img = rotation_right(img, "rotate_right")
# rotation_right(img, "rotate_right")
# It works since rotate 4 times kept the same img
# img = rotation_left(img, "rotate_left")
# img = rotation_left(img, "rotate_left")
# img = rotation_left(img, "rotate_left")
# rotation_left(img, "rotate_left")

# Invert Color test -------------------------------------
# invert_single_rgb(img,"invert_Blue", 0)
# invert_single_rgb(img,"invert_Green", 1)
# img = invert_single_rgb(img,"invert_Red", 2)
# img = invert_single_rgb(img,"invert_red_Green", 1)
# invert_single_rgb(img,"invert_ALL_COlor", 0)
# invert_color(img, "invertedColor")

img = loadImg("./img/aniaa.jpg")

# Test Change Hue
# for i in range(255):
#     print("blue", i)
#     change_hue_1_modes(img, "ahue_Blue" + str(i), i,0)
# for i in range(255):
#     print("Green", i)
#     change_hue_1_modes(img, "bhue_Green" + str(i), i,1)

# change_hue_1_modes(img, "ahue_Blue" + str(255), 255,0)
# change_hue_1_modes(img, "bhue_Green" + str(255), 255,1)

# for i in range(132,256):
#     print("Red", i)
#     change_hue_1_modes(img, "chue_Red" + str(i), i,2)
# for i in range(256):
#     print("C1", i)
#     change_hue_2_modes(img, "dhue_C1" + str(i), i,0,1)
# for i in range(256):
#     print("C2", i)
#     change_hue_2_modes(img, "ehue_C2" + str(i), i,0,2)
# for i in range(256):
#     print("C3", i)
#     change_hue_2_modes(img, "fhue_C3" + str(i), i,1,2)
# for i in range(256):
#     print("invert", i)
#     change_hue_3_modes(img, "ghue_invert" + str(i), i,0,1,2)
# print("COMPLTED!")
img = loadImg("./img/aniaa.jpg")
outputFile(img, "raw img")
# img1 = half_reversion_bonus_LR(img,"LR")
# img2 = half_reversion_bonus_UD(img,"UD")

# img1 = half_reversion_bonus_UD(img1, "LR THEN UD")
# img2 = half_reversion_bonus_LR(img2, "UD THEN LR")
img = Edge_Detection_Function(img, "UDLREDGE", 3)
# img = avgImprovedScale(img, "UDLREDGEGSR")