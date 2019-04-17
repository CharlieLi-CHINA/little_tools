# -*- coding: utf-8 -*-
"""
Created on Tues Aug 07 08:51:19 2018
@author: Charlie
fuction:阈值法辅助lc算法
"""
import cv2,math,sys,os

def yuzhifa(img,picturename):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray = img.copy()
    #hight, width = gray.shape[:2]
    yuzhi = 5
    try:
        
        while yuzhi < 200:  # 寻找阈值和box
            _, thresh = cv2.threshold(gray, yuzhi, 255, cv2.THRESH_BINARY)  # 二值化
            # _, thresh = cv2.threshold(thresh, yuzhi, 255, cv2.THRESH_BINARY_INV)
            # #闭操作/开操作
            kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))  # 横，纵
            kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
            kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_2)  # 闭运算先腐蚀再膨胀,消除离散点
            open = cv2.morphologyEx(close, cv2.MORPH_OPEN, kernel_2)  # 开运算先膨胀再腐蚀,填充图像的内部孔洞和图像的凹角点
            #pengzhang = cv2.dilate(open, kernel_2, iterations=1)  # 膨胀一次，让轮廓突出
            #fushi = cv2.erode(pengzhang, kernel_3, iterations=1)  # 腐蚀一次，去掉细节
            #pengzhang2 = cv2.dilate(fushi, kernel_2, iterations=1)  # 再次膨胀，让轮廓明显一些
            print(yuzhi)
            yuzhi += 5
            cv2.imshow(str(picturename),thresh)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        while True:
            pass
    except KeyboardInterrupt,e:
        print ("you stop the threading")        
def erzhihua(img,yuzhi):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, thresh = cv2.threshold(gray, yuzhi, 255, cv2.THRESH_BINARY)  # 二值化
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)  # 闭运算先腐蚀再膨胀,消除离散点
    open = cv2.morphologyEx(close, cv2.MORPH_OPEN, kernel)  # 开运算先膨胀再腐蚀,填充图像的内部孔洞和图像的凹角点
    cv2.imshow("img",close)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def yuzhifa(img1,pic1,img2,pic2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    yuzhi = 5
    try:
        
        while yuzhi < 200:  # 寻找阈值和box
            _, thresh1 = cv2.threshold(gray1, yuzhi, 255, cv2.THRESH_BINARY)  # 二值化
            _, thresh2 = cv2.threshold(gray2, yuzhi, 255, cv2.THRESH_BINARY)  # 二值化
            print(yuzhi)
            yuzhi += 5
            cv2.imshow(str(pic1),thresh1)
            cv2.imshow(str(pic2),thresh2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        while True:
            pass
    except KeyboardInterrupt,e:
        print ("you stop the threading")        
if __name__ == '__main__':
    path1 = "./0002113.jpg"
    path2 = "./0002113_final.jpg"
    img1 = cv2.imread(path1)
    #yuzhifa(img)
    #erzhihua(img,45)
#    yuzhifa(img,"yuanlai")
   
    img2 = cv2.imread(path2)
    yuzhifa(img1,"yuanlai",img2,"xinde")
    

