import glob
import cv2
import os

image_path = "E:/Sem5/AIP391/src/Character_detection_with_SVM/Raw_data/dataset_characters/"
write_path = "E:/Sem5/AIP391/src/Character_detection_with_SVM/data2/"

char_w = 30
char_h = 60

for number in range(10):
    for img_org_path in  glob.iglob(image_path + str(number) + "/*.jpg"):

        img = cv2.imread(img_org_path, 0)
        img = cv2.resize(img, dsize = (char_w, char_h) ) 

        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # cv2.imshow('after threshold', img)
        # cv2.waitKey()


        print(img_org_path)
        # print(os.path.basename(img_org_path))
        img_org_path = os.path.basename(img_org_path)

        re_path = write_path + str(number)
        print(re_path)
        
        if not os.path.isdir(re_path):
            os.mkdir(re_path)

        # print(os.path.isdir(image_path + str(number)))
        cv2.imwrite(re_path + "/" + img_org_path, img)
        # print( os.listdir(write_path) )
        

for alphabet in range(65,91):
    alph_org_base = chr(alphabet)
    for img_org_path in glob.iglob(image_path + str(alph_org_base) + "/*.jpg"):
        img = cv2.imread(img_org_path, 0)
        img = cv2.resize(img, dsize = (char_w, char_h))

        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        img_org_path = os.path.basename(img_org_path)

        re_path = write_path + str(ord(alph_org_base))
        print(re_path)
        
        if not os.path.isdir(re_path):
            os.mkdir(re_path)

        # print(os.path.isdir(image_path + str(number)))
        cv2.imwrite(re_path + "/" + img_org_path, img)
        