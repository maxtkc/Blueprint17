from PIL import Image
import os
import itertools
import operator

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

        for length in range(1, 40):
            for height in range(1, 30):
                rgb_im = img.convert('RGB')
                r, g, b = rgb_im.getpixel((length, height))
                if r != 255 and g != 255 and b!= 255:
                    listr.append(r)
                    listg.append(g)
                    listb.append(b)

        self.r = self.mostCommon(listr)
        self.g = self.mostCommon(listg)
        self.b = self.mostCommon(listb)


class ImageSorter:
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    images = []

    def __init__(self):
        for filename in os.listdir('icons'):
            if "png" in filename:
                filename = os.path.join(self.fileDir, 'icons/' + filename)
                self.images.append(Icon(filename))

    def getBestImage(self, cv_r, cv_g, cv_b, images):
        total_rgb_list = []

        for icon in images:
             new_r = abs(icon.r - cv_r)
             new_g = abs(icon.g - cv_g)
             new_b = abs(icon.b - cv_b)

             total_rgb = new_r + new_g + new_b
             total_rgb_list.append(total_rgb)

        low = total_rgb_list[0]
        for total_rgb in total_rgb_list:
             if total_rgb < low:
                  low = total_rgb

        low_location = total_rgb_list.index(low)
        image = images[low_location]
        return image


program = ImageSorter()
print "halfway"
ImageSorter.getBestImage(program, 10, 50, 70, program.images)
print "done"

'''
filename = os.path.join(fileDir, 'icons/2.png')
img = Image.open(filename)
rgb_im = img.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))
print r
print g
print b
'''

