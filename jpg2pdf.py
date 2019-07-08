# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:33:15 2019

@author: liqilv
run: python xxx.py xx.jpg
"""

import os
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
f = sys.argv[1]
filename = ''.join(f.split('/')[-1:])[:-4]
f_jpg = filename+'.jpg'
print (f_jpg)
def conpdf(f_jpg):
    f_pdf = filename+'.pdf'
    (w, h) = landscape(A4)
    c = canvas.Canvas(f_pdf, pagesize = landscape(A4))
    c.drawImage(f, 0, 0, w, h)
    c.save()
    print ("okkkkkkkk.")
 
conpdf(f_jpg)