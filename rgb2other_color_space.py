# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:36:51 2019

@author: liqilv
data/
    001/
        xxx.jpg
        xxy.jpp
        xxu.jpg
    002/
        xxx.jpg
        xxy.jpp
        xxu.jpg
    003/
        xxx.jpg
        xxy.jpp
        xxu.jpg
    ...

run in windows python2: python xxx.py [origin_data_path] [new_data_path]
sample: python .\rgb2hsv_0411.py .\data\ .\data2\
"""

import cv2,os,sys

def read_all_folder_path(path):#返回某个目录下的所有的文件夹

    pic_path=  []
    for file in os.listdir(path):
        class_floder_name = str(file)
        class_floder_path = os.path.join(path , class_floder_name)
        pic_path.append(class_floder_path)
    # print(pic_path)
    return pic_path
def rgb2hsv_ycrcb(image_path,save_new_color_space_path):#使用cv2将rgb图像变成其他空间的图像，注：rgb图像在cv2里面是bgr
    #image_path是图像的文件夹路径,save_new_color_space_path是保存的输出文件夹路径
    filenames = os.listdir(image_path)
    print("image quantity: ",len(filenames))
    for filename in filenames:
        examname = filename[:-4]
        type = filename.split('.')[-1]
        img = cv2.imread(image_path + '\\'+ filename)
        img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        save_hsv = save_new_color_space_path + '\\' + examname + '_HSV' + '.' + type
        cv2.imwrite(save_hsv, img_hsv)
        # img_ycrcb = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
        # save_ycrcb = save_path_ycrcb +'\\'+ examname + '_YCrCb' + '.' + type
        # cv2.imwrite(save_ycrcb, img_ycrcb)
def batch_run(data_folder_sum,save_folder_sum):
    print("data_folder quantity: ",len(data_folder_sum))
    for folder in data_folder_sum:
        folder = str(folder)
        folder_name = folder.split('\\')[-1]#获取图像的上一级文件夹名字

        save_new_color_space_path = os.path.join(save_folder_sum, folder_name)
        isExist = os.path.exists(save_new_color_space_path)  # 如果不存在就新建一个文件夹
        if not isExist:
            os.mkdir(save_new_color_space_path)

        rgb2hsv_ycrcb(folder, save_new_color_space_path)
    print("over")

#        print(folder,"--",floder_name,"--",save_new_color_space_path,"--",save_path_ycrcb)
if __name__ == '__main__':
    if len(sys.argv) > 2:  # 依次输入旧的data和新的data路径
        origin_path = sys.argv[1]
        save_folder_sum = sys.argv[2]
    else:
        origin_path = "D:\\GitHub\\little_tools\\data"
        save_folder_sum = "D:\\GitHub\\little_tools\\data2"
    data_folder_sum = read_all_folder_path(origin_path)
    batch_run(data_folder_sum, save_folder_sum)

