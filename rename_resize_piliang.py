# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:19:30 2019
批量重命名和进行resize到同一个尺寸
@author: liqilv
run in windows,python2 
run : python xxx.py [all_class_folder_path]
sample in windows : python xxx.py D:\\Anaconda2\\liqilv\\data_car_color\\test
data_folder---
old:
data
    cars
        xxx.jpg
        xxy.jpg
        ...
    dogs
        xxx.jpg
        xxy.jpg
        ...
    ...
------------------------
new:
data2
    cars
        xxx.jpg
        xxy.jpg
        ...
    dogs
        xxx.jpg
        xxy.jpg
        ...
    ...    


"""
import os,sys,random,glob
from PIL import Image

def tiqi_floder_name(path):#获取输入路径的最后文件夹名字
    floder_name = path.split('\\')[-1]
    return floder_name

def convertjpg(jpgfile,outdir,width=224,height=224):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)

def rename(path,class_pre,old_type=".jpg",new_type=".jpg"):#原地重命名
    
    filelist = os.listdir(path)

    i = 0
    random_number = str(random.randint(11, 99))#解决重命名一次后，再次操作形成的新文件会受到原来文件影响
    
    for item in filelist:
        if item.endswith(old_type):
            src = os.path.join(os.path.abspath(path), item)
            bianhao = str(i).zfill(5)
            dst = os.path.join(os.path.abspath(path), class_pre + random_number+ "_" + bianhao + new_type)
            os.rename(src, dst)
            i = i + 1
def piliang(path):
    print("piliang")
    new_sum_path = path + "2"
    
    isExist = os.path.exists(new_sum_path)#如果不存在就新建一个文件夹
    if not isExist:
        os.mkdir(new_sum_path)#新的总目录与原来总目录不一样，但是与原来目录同级
        
    for file in os.listdir(path):
        class_floder_name = str(file)
        class_floder_path = os.path.join(path , class_floder_name)
        rename(class_floder_path,class_floder_name)
        
        new_floder = os.path.join(new_sum_path , class_floder_name)
        isExist = os.path.exists(new_floder)#如果不存在就新建一个文件夹
        if not isExist:
            os.mkdir(new_floder)
        for jpgfile in glob.glob(class_floder_path+"\\*.jpg"):#
            convertjpg(jpgfile,new_floder) 
    print("piliang-end")
        
if __name__ == '__main__':
    sum_path = sys.argv[1] if len(sys.argv) > 1 else "D:\\Anaconda2\\liqilv\\data_car_color\\test" # 输入路径
    piliang(sum_path)
            