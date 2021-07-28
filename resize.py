import cv2
import os

#
def resize():
    path = 'path of images' # change this before run the code
    d_path = 'path for new images'# change this before run the code
    filelist = os.listdir(path)
    i = 1
    for item in filelist:
        if item.endswith('.jpg'): # you can chaneg file extention to , '.jpeg', '.png'
            src = os.path.join(os.path.abspath(path), item)
            dst = os.path.join(os.path.abspath(d_path), 'rabbit.' + str(i) + '.jpg')
            i += 1
            src_img = cv2.imread(src)
            dest_img = cv2.resize(src_img, (300, 300), interpolation=cv2.INTER_CUBIC) # you can change new image size (300, 300) to any image size
            cv2.imwrite(dst, dest_img)


if __name__ == "__main__":
    resize()


