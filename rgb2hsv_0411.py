# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:36:51 2019

@author: liqilv
"""

import cv2,os

#image_path ='F:\\test\\image1\\'
#
#save_path_hsv = 'F:\\test\\image1\\'
#
#save_path_ycrcb = 'F:\\test\\image1\\'

train_origin_path = "D:\\Anaconda2\\liqilv\\litle_tool\\rgb2hsv\\data\\train"
val_origin_path = "D:\\Anaconda2\\liqilv\\litle_tool\\rgb2hsv\\data\\validation"

hsv_train_path = "D:\\Anaconda2\\liqilv\\litle_tool\\rgb2hsv\\hsv\\train"
hsv_val_path = "D:\\Anaconda2\\liqilv\\litle_tool\\rgb2hsv\\hsv\\val"

ycrcb_train_path = "D:\\Anaconda2\\liqilv\\litle_tool\\rgb2hsv\\ycrcb\\train"
ycrcb_val_path = "D:\\Anaconda2\\liqilv\\litle_tool\\rgb2hsv\\ycrcb\\val"

def read_folder_name2pic_path(path):

    pic_path=  []
    for file in os.listdir(path):
        class_floder_name = str(file)
        class_floder_path = os.path.join(path , class_floder_name)
        pic_path.append(class_floder_path)
    # print(pic_path)
    return pic_path
def brg2hsv_ycrcb(image_path,save_path_hsv,save_path_ycrcb):
    filenames = os.listdir(image_path)
    for filename in filenames:
        examname = filename[:-4]
        type = filename.split('.')[-1]
        img = cv2.imread(image_path + '\\'+ filename)
        img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        img_ycrcb = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
        save_hsv = save_path_hsv +'\\'+ examname + '_HSV'+'.'+type
        save_ycrcb = save_path_ycrcb +'\\'+ examname + '_YCrCb' + '.' + type
        cv2.imwrite(save_hsv,img_hsv)
        cv2.imwrite(save_ycrcb, img_ycrcb)

if __name__ == '__main__':
#    brg2hsv_ycrcb(image_path, save_path_hsv, save_path_ycrcb)
    train_pic_path = read_folder_name2pic_path(train_origin_path)
    val_pic_path = read_folder_name2pic_path(val_origin_path)
    
    #train-data
    for folder in train_pic_path:
        folder = str(folder)
        floder_name = folder.split('\\')[-1]
        
        save_path_hsv = os.path.join(hsv_train_path , floder_name)
        isExist = os.path.exists(save_path_hsv)#如果不存在就新建一个文件夹
        if not isExist:
            os.mkdir(save_path_hsv)
#        print(folder,"--",floder_name,"--",save_path_hsv)
        
        save_path_ycrcb = os.path.join(ycrcb_train_path , floder_name)
        isExist = os.path.exists(save_path_ycrcb)#如果不存在就新建一个文件夹
        if not isExist:
            os.mkdir(save_path_ycrcb)
#        print(folder,"--",floder_name,"--",save_path_hsv,"--",save_path_ycrcb)
        
        brg2hsv_ycrcb(folder, save_path_hsv, save_path_ycrcb)
    print("train--over")    
    #val-data
    for folder in val_pic_path:
        folder = str(folder)
        floder_name = folder.split('\\')[-1]
        
        save_path_hsv = os.path.join(hsv_val_path , floder_name)
        isExist = os.path.exists(save_path_hsv)#如果不存在就新建一个文件夹
        if not isExist:
            os.mkdir(save_path_hsv)
#        print(folder,"--",floder_name,"--",save_path_hsv)
        
        save_path_ycrcb = os.path.join(ycrcb_val_path , floder_name)
        isExist = os.path.exists(save_path_ycrcb)#如果不存在就新建一个文件夹
        if not isExist:
            os.mkdir(save_path_ycrcb)
#        print(folder,"--",floder_name,"--",save_path_hsv,"--",save_path_ycrcb)
        
        brg2hsv_ycrcb(folder, save_path_hsv, save_path_ycrcb)
    print("val--over")   