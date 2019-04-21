# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:51:56 2019

@author: liqilv

读取目录下面的文件夹或者文件名字，将其写到txt里面
run in windows python
sample: pyton xxx.py [folder_path] [save_path]
run in win10 for python 2.7/3.6 :   python .\get_folder2_txt.py .\data .
"""
import os,sys
import numpy as np

def read_and_wirte(path,save_path):
    file_list = os.listdir(path)
    txt_data_lie = []
    i = 0
    for file in file_list:
        file = str(i) + ":" + str(file)#随意添加东西，可以是序号
        txt_data_lie.append(str(file))
        i += 1
    name_data = np.array(txt_data_lie)
    np.savetxt(os.path.join(save_path,"result.txt"), name_data,fmt="%s")#fmt="%s" is the str format
if __name__ == '__main__':
    
    if len(sys.argv) > 2:  # 依次输入文件夹或者文件存放的路径、保存的文件路径
        
        folder_path = sys.argv[1]
        save_path = sys.argv[2]
    else:
        
        folder_path = "D:\\GitHub\\little_tools\\data"
        save_path = "D:\\GitHub\\little_tools"
    read_and_wirte(folder_path,save_path)