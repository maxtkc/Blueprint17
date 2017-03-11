from PIL import Image
import os
import itertools
import operator
import cv2
import numpy as np

class Icon:
    r = 255
    g = 255
    b = 255
    name = ""


    def mostCommon(self, L):

        SL = sorted((x, i) for i, x in enumerate(L))
        groups = itertools.groupby(SL, key=operator.itemgetter(0))

        def common(g):
            item, iterable = g
            count = 0
            min_index = len(L)

            for _, where in iterable:
                 count += 1
                 min_index = min(min_index, where)

            return count, -min_index

        return max(groups, key=common)[0]

    def __init__(self, filename):
        img = Image.open(filename)
        self.name = filename

        listr = []
        listg = []
        listb = []

        rgb_im = img.convert('RGB')

        for length in range(1, 40):
            for height in range(1, 30):
                r, g, b = rgb_im.getpixel((length, height))
                if r != 255 and g != 255 and b!= 255:
                    listr.append(r)
                    listg.append(g)
                    listb.append(b)

        self.r = self.mostCommon(listr)
        self.g = self.mostCommon(listg)
        self.b = self.mostCommon(listb)
        # pix = cv2.resize(cv2.imread(filename), (1, 1))[0,0]
        # self.r = pix[0]
        # self.g = pix[1]
        # self.b = pix[2]
        # print self.r,self.g,self.b


class ImageSorter:
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    images = []

    def __init__(self):
        counter = 0
        for filename in os.listdir('cartoons'):
            if True:
                filename = os.path.join(self.fileDir, 'cartoons/' + filename)
                self.images.append(Icon(filename))
                # if counter == 200:
                #     break
                print counter
                counter +=1

    def getBestImage(self, cv_r, cv_g, cv_b, images):
        # total_rgb_list = []

        # for icon in images:
        #      new_r = abs(icon.r - cv_r)
        #      new_g = abs(icon.g - cv_g)
        #      new_b = abs(icon.b - cv_b)

        #      total_rgb = new_r + new_g + new_b
        #      total_rgb_list.append(total_rgb)

        # low = total_rgb_list[0]
        # for total_rgb in total_rgb_list:
        #      if total_rgb < low:
        #           low = total_rgb

        # low_location = total_rgb_list.index(low)
        # image = images[low_location]

        best_image = None
        closest_distance = 10**4

        for icon in images:
            d = abs(cv_r - icon.r)
            if (d < closest_distance):
                closest_distance = d
                best_image = icon

            d = abs(cv_g - icon.g)
            if (d < closest_distance):
                closest_distance = d
                best_image = icon

            d = abs(cv_b - icon.b)
            if (d < closest_distance):
                closest_distance = d
                best_image = icon

        return best_image


# program = ImageSorter()
# print "halfway"
# ImageSorter.getBestImage(program, 10, 50, 70, program.images)
# print "done"

'''
filename = os.path.join(fileDir, 'icons/2.png')
img = Image.open(filename)
rgb_im = img.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))
print r
print g
print b
'''
