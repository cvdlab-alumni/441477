# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:19:15 2014

@author: chiara
"""


from pyplasm import CUBOID
from pyplasm import VIEW
from pyplasm import R
from pyplasm import T
from pyplasm import COLOR
from pyplasm import STRUCT
from pyplasm import NN
from pyplasm import DIFF
from pyplasm import PROD
from pyplasm import INSR
from pyplasm import CYLINDER
from pyplasm import Color4f
from pyplasm import PI
from pyplasm import MK
from pyplasm import JOIN
from pyplasm import Q
from pyplasm import QUOTE
from pyplasm import MAP
from pyplasm import COS
from pyplasm import SIN
from pyplasm import BEZIER
from pyplasm import INTERVALS
from pyplasm import S3



#function to define color
def colorRGB(values):
        return Color4f([ values[0]/255.0,
                         values[1]/255.0,
                         values[2]/255.0,
                         1.0])
                
green = colorRGB([60,179,113])
colorFloor2 = colorRGB([204,153,102])
colorCubi = colorRGB([204,119,34])

#stairs
colorStair = colorRGB([152,118,84])
stair1=T([1,2,3])([-0.5,-0.5,-0.5])(CUBOID([8,15,0.5]))
stair2=T([1,2,3])([-1,-1,-1])(CUBOID([9,16,0.5]))
stair3=T([1,2,3])([-1.5,-1.5,-1.5])(CUBOID([10,17,0.5]))
stairs=COLOR(colorStair)(STRUCT([stair1,stair2,stair3]))
#floor0 = base
floor0 = COLOR(colorFloor2)(CUBOID([7,14,0.5]))
#central elements
centralColumn = [T(1)(0.9),CYLINDER([0.25,5])(10)]
colorCentralElement = colorRGB([143,188,143])
brown = colorRGB([112,66,20])
a = T([1,2,3])([1.8,2,0.5])(CUBOID([0.3,3,5]))  #segment of the central structure
b = T([1,2,3])([5,2,0.5])(CUBOID([0.3,3,5]))    #segment of the central structure
c = T([1,2,3])([5,9,0.5])(CUBOID([0.3,3,5]))    #segment of the central structure
d = T([1,2,3])([1.8,9,0.5])(CUBOID([0.3,3,5]))  #segment of the central structure
column_sud_central =  T([1,2,3])([2.2,2.25,0.5])((STRUCT(NN(2)(centralColumn))))
column_nord_central =  T([1,2,3])([2.2,11.75,0.5])((STRUCT(NN(2)(centralColumn))))
rect_est = T([1,2,3])([5,5,0.5])(INSR(PROD)(([Q(0.3),QUOTE([-0.4,0.3]*5),Q(5)])))
rect_ovest = T([1,2,3])([1.8,5,0.5])(INSR(PROD)(([Q(0.3),QUOTE([-0.4,0.3]*5),Q(5)])))
rect_up_est = T([1,2,3])([5,5,3.5])(CUBOID([0.3,4,2]))
rect_up_ovest = T([1,2,3])([1.8,5,3.5])(CUBOID([0.3,4,2]))
#triangular element of the central structure
rectC = T([1,2,3])([1.8,2,5.5])(CUBOID([3.5,0.5,0.5]))
ptC = MK([3.5,2.3,7])
centralFront = JOIN([rectC,ptC])
rect_nord = T([2,3])([9.5,-0.5])(rectC)
#final central structure
central = COLOR(brown)(STRUCT([a,b,c,d,column_sud_central,column_nord_central,rect_est,rect_ovest,centralFront,rect_up_est,rect_up_ovest,rect_nord]))

solid_model_3D = STRUCT([floor0,central,stairs])

VIEW(solid_model_3D)
