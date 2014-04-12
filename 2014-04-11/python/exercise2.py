# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:03:00 2014

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


#floor1 = upper part of the columns
cubo = CUBOID([0.5,-0.5,0.2])
cubi = [T(1)(0.9), cubo]
cubi_sud = T([2,3])([1,5.8])((STRUCT(NN(6)(cubi))))
cubi_nord = T([2,3])([13.5,5.8])((STRUCT(NN(6)(cubi))))
cubi_ovest = R([1,2])(PI/2)(T([1,2,3])([0.5,-0.5,5.8])(((STRUCT(NN(13)(cubi))))))
cubi_est =  R([1,2])(PI/2)(T([1,2,3])([0.5,-6,5.8])(((STRUCT(NN(13)(cubi))))))
floor1 = COLOR(colorCubi)(STRUCT([cubi_sud,cubi_nord,cubi_ovest,cubi_est]))
#floor2 = cornice on the columns
element1 = T([1,2,3])([1,1,6])(CUBOID([5,12,0.5]))
element2 = T([1,2,3])([0.5,0.5,6])(CUBOID([6,13,0.5]))
floor2 = COLOR(colorFloor2)(DIFF([element2,element1]))
floor2 = COLOR(colorFloor2)(DIFF([element2,element1]))
#horizontal elements
cornice=STRUCT([floor1,floor2])
#columns
colorColumns = colorRGB([255,204,153])
column = [T(1)(0.9),CYLINDER([0.25,5.3])(10)]
columns_sud = T([1,2,3])([0.25,13.25,0.5])((STRUCT(NN(6)(column))))
columns_nord = T([1,2,3])([0.25,0.75,0.5])((STRUCT(NN(6)(column))))
columns_est =  R([1,2])(PI/2)(T([1,2,3])([0.75,-6.25,0.5])(((STRUCT(NN(13)(column))))))
columns_ovest = R([1,2])(PI/2)(T([1,2,3])([0.75,-0.75,0.5])(((STRUCT(NN(13)(column))))))
columns = COLOR(colorColumns)(STRUCT([columns_sud,columns_nord,columns_est,columns_ovest]))
#triangular front element
rect = T([1,2,3])([0.7,0.6,6.5])(CUBOID([5.6,0.3,0.5]))
pt = MK([3.35,0.45,8.5])
front = COLOR(colorCubi)(JOIN([rect,pt]))
#triangular back element
rect_back = T(2)(12.5)(rect)
pt_back = MK([3.15,13.2,8])
back = COLOR(colorCubi)(JOIN([rect_back,pt_back]))
#decorations
decor = [T(1)(0.55), CUBOID([0.2,-0.3,0.45])]
decoration_s = T([1,2,3])([0.1,0.7,6.5])((STRUCT(NN(11)(decor))))
plane = T([1,2,3])([0.6,0.4,7])(CUBOID([5.8,0.6,0.1]))
decoration_sud = STRUCT([decoration_s,plane])
decoration_nord = T([1,2])([7,14])(R([1,2])(PI)(decoration_sud))
decoration = STRUCT([decoration_sud,decoration_nord])
plane2 = R([1,3])(PI/6)(T([1,2,3])([4.1,0.2,5.7])(CUBOID([3.1,0.6,0.1])))
plane3 = R([1,3])(-PI/6.2)(T([1,2,3])([-1.2,0.2,9.1])(CUBOID([3.1,0.6,0.1])))
decorations = STRUCT([decoration,plane2,plane3])
#vertical structure
vertical_mock_up_3D = STRUCT([columns,front,back,decorations])
solid_vertical_model_3D = STRUCT([cornice,vertical_mock_up_3D])

VIEW(solid_vertical_model_3D)

