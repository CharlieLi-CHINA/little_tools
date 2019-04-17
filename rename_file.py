# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:09:18 2018
批量重命名文件，可以选择后缀

@author: liqilv
use: python rename.py [filepath] [old file type] [new file type]
sample in windows : python rename_file.py D:\\Anaconda2\\liqilv\\litle_tool\\rename\\red .jpg .jpg
"""


import os,sys
import random

def tiqi_folder_name(path):#获取输入路径的最后文件夹名字
    folder_name = path.split('\\')[-1]
    return folder_name

def rename(path,color,old_type,new_type):
    
    filelist = os.listdir(path)

    i = 0

    for item in filelist:
        if item.endswith(old_type):#不是指定的文件类型，不会执行
            src = os.path.join(os.path.abspath(path), item)#旧路径

            bianhao = str(i).zfill(5)#以0填充到5位数字
#            biaohao = str(random.randint(2,20000)).zfill(5)
#            biaohao = str(random.randrange(2, 20000, 2)).zfill(5)#偶数命名
            dst = os.path.join(os.path.abspath(path), color + "_" + bianhao + new_type)#新路径
            os.rename(src, dst)

            i = i + 1

if __name__ == '__main__':
    if len(sys.argv) > 1:  # 读取参数名作为文件名
        path = sys.argv[1]
                       
    else:
        path = "D:\\Anaconda2\\liqilv\\litle_tool\\rename\\red"
     
    old_type = sys.argv[2] if len(sys.argv) > 2 else ".jpg" # 输入类别
    new_type = sys.argv[3] if len(sys.argv) > 3 else ".jpg"# 重命名类别
    
    folder_name = tiqi_folder_name(path)#提取输入文件夹的名字，重命名以文件夹名字为前缀
    folder_name = str(folder_name)
    
    rename(path,folder_name,old_type,new_type)
    
    