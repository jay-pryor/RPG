from PIL import Image
from numpy import asarray
class Art():
    def __init__(self, pic_name):
        self.img_map = []
        ## Only works with image files named as follows: image_name123567.format
        ## where 123 is desired picture horizontal length & 567 is desired
        ## picture vertical height

        ## Opens image, converts colour format to RGB, formats
        ## picture as numpy array

        image = Image.open(pic_name)
        image = image.convert('RGB')
        picture = asarray(image)

        ## Find and records resolution of image

        info = image.size
        h_res = info[0]
        v_res = info[1]

        ## Retrieves desired picture pixel resolution from title

        pos = pic_name.index('.')
        pic_name_cut = pic_name[:pos]
        h_pic_res = pic_name_cut[-6:-3]
        v_pic_res = pic_name_cut[-3:]

        # print(h_pic_res)
        # print(v_pic_res)

        ## Divides real resolution into desired resolution chunks

        h_div = int(int(h_res) / int(h_pic_res))
        v_div = int(int(v_res) / int(v_pic_res))

        ## Creates list with appropriate amount of sublists to contain all pixels

        for i in range(int(v_pic_res)):
            self.img_map.append([])

            ## Goes through image and retrieves RGB colour values of each pixel
            ## and stores them as a list within the appropriate sublist for that
            ## pixel i.e. [[[0, 0, 0]],[],[]]

            # print(range(int(v_pic_res)))
            # print(range(int(h_pic_res)))

        for i in range(int(v_pic_res)):
            for n in range(int(h_pic_res)):
                x_val = 2 + n * v_div
                y_val = 2 + i * h_div

                # print('hos', x_val, n)
                # print('vert', y_val, i)

                col = picture[x_val, y_val]
                self.img_map[n].append((col.tolist())[:3])
        self.h = len(self.img_map)
        self.w = len(self.img_map)



























