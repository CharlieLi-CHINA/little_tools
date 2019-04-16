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
    total_num = len(filelist)

    i = 0

    for item in filelist:
        if item.endswith(old_type):
            src = os.path.join(os.path.abspath(path), item)
#                dst = os.path.join(os.path.abspath(path), '00100' + format(str(i), '0>3s') + '.jpg')
            bianhao = str(i).zfill(5)
            dst = os.path.join(os.path.abspath(path), color + "_" + bianhao + new_type)
            os.rename(src, dst)
#                print ('converting %s to %s ...' % (src, dst))
            i = i + 1
#        print ('total %d to rename & converted %d jpgs' % (total_num, i))        
#rename()
if __name__ == '__main__':
    if len(sys.argv) > 1:  # 读取参数名作为文件名
        path = sys.argv[1]
                       
    else:
        path = "D:\\Anaconda2\\liqilv\\litle_tool\\rename\\red"
     
    old_type = sys.argv[2] if len(sys.argv) > 2 else ".jpg"
    new_type = sys.argv[3] if len(sys.argv) > 3 else ".jpg"
    
    folder_name = tiqi_folder_name(path)
    folder_name = str(folder_name)
    rename(path,folder_name,old_type,new_type)
    
    