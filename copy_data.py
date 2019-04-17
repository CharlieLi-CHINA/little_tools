# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:26:12 2019

@author: liqilv

copy data acoording the txt file and class by the txt name 
"""

import os,sys
import shutil
import numpy as np

abspath = "D:\\Anaconda2\\liqilv\\litle_tool\\copy_data_big_amount\\"

dataset_path = "E:\\dataset_from_bk\\VehicleID_V1.0\\VehicleID_V1.0\\image\\"
txt_folder_path = "D:\\Anaconda2\\liqilv\\litle_tool\\copy_data_big_amount\\txt_file_name\\"
dataset_path_new = "D:\\Anaconda2\\liqilv\\litle_tool\\copy_data_big_amount\\color_file_new\\"

data_test_path = "E:\\dataset_from_bk\\test\\"
data_new_path = "E:\\dataset_from_bk\\test2\\"
txt_file_name = "E:\\dataset_from_bk\\tt.txt"

def copy_picture(old_path,new_path):
    dataset_list=os.listdir(old_path)
    
    for i in dataset_list:
        oldname = old_path + i
        newname = new_path + i
#        aa,bb=i.split(".")
        print("okkk")
#        if 'python' in aa.lower():
#            print("ok")
#            oldname = path + aa + "." + bb
#            newname = "E:\\dataset_from_bk\\test2\\" + aa + "." + bb
        shutil.copyfile(oldname,newname)

def recoder_none_name2txt(txt_data,class_number):#填充数字，保证7位,并保存成txt和命名

    name_data = []
    for data in txt_data:
        edata = str(data).zfill(7)
        name_data.append(edata)
    name_data = np.array(name_data)
#    print(name_data)
    np.savetxt(file_path+str(class_number)+"_result.txt", name_data,fmt="%s")#fmt="%s" is the str format

def copy_txt_filename(txt_path,old_path,new_path):
    
    jpg_name = open(txt_path)
    non_name = []
    jishu = 0
    for i in jpg_name:
        # 找对应的图片
        i = i.strip('\n')   #去掉换行符
        if jishu%100 == 0:
            print("========")
            print("mount is :"+str(jishu))
            print("========")
        jishu += 1
        try:
            src=os.path.join(os.path.abspath(old_path),i + '.jpg')
            # 重命名,改为jpg格式
            dst=os.path.join(os.path.abspath(new_path),i + '.jpg')
            # 执行操作,复制文件
            shutil.copyfile(src,dst)
        except (IOError ,ZeroDivisionError):#如果txt里面的文件名在数据集里没有就跳过
            print("No such file: "+str(i)+".jpg"+ ", please next one")
            non_name.append(str(i))
            
    non_name = np.array(non_name)
    txtname = txt_path.split('\\')[-1][:-4]
    np.savetxt(abspath+txtname+"_non_name.txt", non_name,fmt="%s")
    
def mut_txt2_pic_fle(txt_folder,data_test_path,save_path_folder):
    
    txt_folder_name = txt_folder.split('\\')[-1][:-4]
    data_new_path = save_path_folder +"\\"+ str(txt_folder_name)+"\\"
    if not os.path.exists(data_new_path):#不存在就新建一个
        os.mkdir(data_new_path)
    
    copy_txt_filename(txt_folder,data_test_path,data_new_path)
    
if __name__=='__main__':
#    copy_picture(data_test_path,data_new_path)
    mut_txt2_pic_fle(sys.argv[1],sys.argv[2],sys.argv[3])
    #sys.argv[1]~[3]分别是txt文档路径、图像数据集路径、要保存的新图像目录
    
    