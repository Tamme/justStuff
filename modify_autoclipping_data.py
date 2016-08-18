import os, sys
import Image
# jpgfile = Image.open("../../pildid/train/1_a.jpg")

# print jpgfile.bits, jpgfile.size, jpgfile.format
# print jpgfile.shape

from scipy import misc
import numpy as np
import copy

for fileIdx in range(909):
    try:

        original = misc.imread("../../pildid/train/" + str(fileIdx) + "_a.jpg")

        cutout = misc.imread("../../pildid/train/" + str(fileIdx) + "_b.png")
        cutout_ours = original.copy()

        #face = misc.imread("../../data/HED-BSDS/train/aug_gt/0.0_1_0/54005.png")
        #face = misc.imread("../../pildid/train/1_c.png")
        #print type(face)
        cutoutInTwoDim = np.sum(cutout, axis = 2)
        #print cutoutInTwoDim
        #input("kkkkk")
        #print cutout.shape
        for i in range(cutout.shape[0]):
            for j in range(cutout.shape[1]):
                if cutoutInTwoDim[i, j] == 0:
                    cutout_ours[i, j, :] = [0, 0, 0]
                else:
                    if i == 0 and j == 0:
                        if (cutoutInTwoDim[i, j+1] == 0 or cutoutInTwoDim[i+1, j]== 0 or cutoutInTwoDim[i+1, j+1]== 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif j == 0 and i == cutout.shape[0] - 1:
                        if (cutoutInTwoDim[i - 1, j] == 0 or cutoutInTwoDim[i - 1, j + 1] == 0 or cutoutInTwoDim[i, j + 1] == 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif i == 0 and j == cutout.shape[1] - 1:
                        if (cutoutInTwoDim[i, j-1] == 0 or cutoutInTwoDim[i + 1, j - 1] == 0 or cutoutInTwoDim[i+1, j] == 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif i == 0:
                        if (cutoutInTwoDim[i, j-1] == 0 or cutoutInTwoDim[i+1, j-1]== 0 or cutoutInTwoDim[i, j+1]== 0 or cutoutInTwoDim[i+1, j+1]== 0 or cutoutInTwoDim[i+1, j]== 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif j == 0:
                        if (cutoutInTwoDim[i-1, j] == 0 or cutoutInTwoDim[i-1, j+1]== 0 or cutoutInTwoDim[i, j+1]== 0 or cutoutInTwoDim[i+1, j+1]== 0 or cutoutInTwoDim[i+1, j]== 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif i == cutout.shape[0]-1 and j == cutout.shape[1] - 1:
                        if (cutoutInTwoDim[i - 1, j] == 0 or cutoutInTwoDim[i - 1, j - 1] == 0 or cutoutInTwoDim[i, j - 1] == 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif i == cutout.shape[0]-1:
                        if (cutoutInTwoDim[i, j-1] == 0 or cutoutInTwoDim[i-1, j-1]== 0 or cutoutInTwoDim[i-1, j]== 0 or cutoutInTwoDim[i-1, j+1]== 0 or cutoutInTwoDim[i, j+1]== 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif j == cutout.shape[1] - 1:
                        if (cutoutInTwoDim[i-1, j] == 0 or cutoutInTwoDim[i - 1, j - 1] == 0 or cutoutInTwoDim[i , j-1] == 0 or cutoutInTwoDim[i + 1, j - 1] == 0 or cutoutInTwoDim[i+1, j] == 0):
                            cutout_ours[i, j, :] = [255, 255, 255]
                    elif cutoutInTwoDim[i-1, j-1] == 0 or cutoutInTwoDim[i-1, j]== 0 or cutoutInTwoDim[i-1, j+1]== 0 or cutoutInTwoDim[i, j-1]== 0  or cutoutInTwoDim[i+1, j-1 ]== 0 or \
                        cutoutInTwoDim[i, j+1] == 0 or cutoutInTwoDim[i+1, j]== 0 or cutoutInTwoDim[i+1, j+1] == 0:
                        cutout_ours[i, j, :] = [255, 255, 255]
                    else:
                        cutout_ours[i, j, :] = [0, 0, 0]
        misc.imsave("../../pildid/train/" + str(fileIdx) + "_c.png", cutout_ours)
        print('finish ' + str(fileIdx))
    except Exception as inst:
     print(type(inst))    # the exception instance
     #print(inst.args)     # arguments stored in .args
     #print(inst)          # __str__ allows args to be printed directly,
                          # but may be overridden in exception subclasses
     #x, y = inst.args     # unpack args
     #print('x =', x)
     #print('y =', y)
     print("missing file " + str(fileIdx))