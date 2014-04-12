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

#stairs
colorStair = colorRGB([152,118,84])
stair1=T([1,2,3])([-0.5,-0.5,-0.5])(CUBOID([8,15,0.5]))
stair2=T([1,2,3])([-1,-1,-1])(CUBOID([9,16,0.5]))
stair3=T([1,2,3])([-1.5,-1.5,-1.5])(CUBOID([10,17,0.5]))
stairs=COLOR(colorStair)(STRUCT([stair1,stair2,stair3]))
#floor0 = base
floor0 = COLOR(colorFloor2)(CUBOID([7,14,0.5]))
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
two_and_half_model=STRUCT([floor0,floor1,floor2])
#columns
colorColumns = colorRGB([255,204,153])
column = [T(1)(0.9),CYLINDER([0.25,5.3])(10)]
columns_sud = T([1,2,3])([0.25,13.25,0.5])((STRUCT(NN(6)(column))))
columns_nord = T([1,2,3])([0.25,0.75,0.5])((STRUCT(NN(6)(column))))
columns_est =  R([1,2])(PI/2)(T([1,2,3])([0.75,-6.25,0.5])(((STRUCT(NN(13)(column))))))
columns_ovest = R([1,2])(PI/2)(T([1,2,3])([0.75,-0.75,0.5])(((STRUCT(NN(13)(column))))))
columns = COLOR(colorColumns)(STRUCT([columns_sud,columns_nord,columns_est,columns_ovest]))
#vertical structure
vertical_mock_up_3D = STRUCT([columns])
solid_model_3D = STRUCT([two_and_half_model,vertical_mock_up_3D,stairs])

VIEW(solid_model_3D)
