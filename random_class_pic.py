# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:00:59 2019
environment windows 10 python2.7
@author: liqilv
随机划分图像为训练和测试集

"""

##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil,sys
abspath = "D:\\Anaconda2\\liqilv\\data_car_color\\cars_11_1000_220_224_224\\train\\"
# D:\Anaconda2\liqilv\data_car_color\car_origin
abs_path_test = "D:\\Anaconda2\\liqilv\\data_car_color\\cars_11_1000_220_224_224\\test\\"
def tiqi_folder_name(path):#获取输入路径的最后文件夹名字
    folder_name = path.split('\\')[-1]
    return folder_name
    
def moveFile(origin_path,new_path,rate):
    pathDir = os.listdir(origin_path)    #取图片的原始路径
    filenumber=len(pathDir)
    # rate=0.1    #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    # picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
    picknumber=int(220) #文件夹中取700数量图片
    sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片
    # print (sample)
    print("==========")
    print("test data mount: " + str(len(sample)) + "/" +str(filenumber))
    print("==========")
    for name in sample:
        shutil.move(origin_path+name, new_path+name)
        
#    return

if __name__ == '__main__':
    if len(sys.argv) > 1:  # 读取参数名作为文件名
        class_folder = sys.argv[1]+"\\"                      
    else:
        class_folder = "pink\\"
    # class_folder = "pink\\"
    origin_path = abspath + class_folder   #源图片文件夹路径
    new_path = abs_path_test + class_folder    #移动到新的文件夹路径
    
    # old_type = sys.argv[2] if len(sys.argv) > 2 else ".jpg"
    # new_type = sys.argv[3] if len(sys.argv) > 3 else ".jpg"
    
    isExist = os.path.exists(new_path)#如果不存在就新建一个文件夹
    if not isExist:
        os.mkdir(new_path)
    rate = 0.2   
    moveFile(origin_path,new_path,rate)




