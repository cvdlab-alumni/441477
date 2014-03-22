# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 07:46:18 2014

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
from pyplasm import Color4f
from pyplasm import PI
from pyplasm import MK
from pyplasm import JOIN
from pyplasm import Q
from pyplasm import QUOTE

#function to define color
def colorRGB(values):
        return Color4f([ values[0]/255.0,
                         values[1]/255.0,
                         values[2]/255.0,
                         1.0])
                

colorFloor2 = colorRGB([204,153,102])
colorCubi = colorRGB([204,119,34])

floor0 = COLOR(colorFloor2)(CUBOID([7,14]))

cubo = CUBOID([0.5,-0.5])
cubi = [T(1)(0.9), cubo]
cubi_sud = T([2,3])([1,5.8])((STRUCT(NN(6)(cubi))))
cubi_nord = T([2,3])([13.5,5.8])((STRUCT(NN(6)(cubi))))
cubi_ovest = R([1,2])(PI/2)(T([1,2,3])([0.5,-0.5,5.8])(((STRUCT(NN(13)(cubi))))))
cubi_est =  R([1,2])(PI/2)(T([1,2,3])([0.5,-6,5.8])(((STRUCT(NN(13)(cubi))))))

floor1 = COLOR(colorCubi)(STRUCT([cubi_sud,cubi_nord,cubi_ovest,cubi_est]))

element1 = T([1,2])([1,1])(CUBOID([5,12]))
element2 = T([1,2])([0.5,0.5])(CUBOID([6,13]))


floor2 = COLOR(colorFloor2)(T(3)(6)((DIFF([element2,element1]))))
two_and_half_model=STRUCT([floor0,floor1,floor2])

colorColumns = colorRGB([255,204,153])

column = [T(1)(0.9),CUBOID([0.25,0,5.3])]
columns_sud = T([1,2,3])([0.25,13.25,0.5])((STRUCT(NN(6)(column))))
columns_nord = T([1,2,3])([0.25,0.75,0.5])((STRUCT(NN(6)(column))))
columns_est =  R([1,2])(PI/2)(T([1,2,3])([0.75,-6.25,0.5])(((STRUCT(NN(13)(column))))))
columns_ovest = R([1,2])(PI/2)(T([1,2,3])([0.75,-0.75,0.5])(((STRUCT(NN(13)(column))))))
columns = COLOR(colorColumns)(STRUCT([columns_sud,columns_nord,columns_est,columns_ovest]))

#triangular front element
rect = T([1,2,3])([0.7,0.6,6.5])(CUBOID([5.6,0,1]))
pt = MK([3.15,0.45,9])
front = COLOR(colorCubi)(JOIN([rect,pt]))
#central structure
centralColumn = [T(1)(0.9),CUBOID([0.25,0,5])]
colorCentralElement = colorRGB([143,188,143])
brown = colorRGB([112,66,20])
a = T([1,2,3])([1.8,2,0.5])(CUBOID([0,3,5])) #segment of the central structure
b = T([1,2,3])([5,2,0.5])(CUBOID([0,3,5]))  #segment of the central structure
c = T([1,2,3])([5,9,0.5])(CUBOID([0,3,5]))  #segment of the central structure
d = T([1,2,3])([1.8,9,0.5])(CUBOID([0,3,5]))    #segment of the central structure
column_sud_central =  T([1,2,3])([2.2,2.25,0.5])((STRUCT(NN(2)(centralColumn))))
column_nord_central =  T([1,2,3])([2.2,11.75,0.5])((STRUCT(NN(2)(centralColumn))))
rect_est = T([1,2,3])([5,5,0.5])(INSR(PROD)(([Q(0),QUOTE([-0.4,0.3]*5),Q(3)])))
rect_ovest = T([1,2,3])([1.8,5,0.5])(INSR(PROD)(([Q(0),QUOTE([-0.4,0.3]*5),Q(3)])))
rect_up_est = T([1,2,3])([5,5,3.5])(CUBOID([0,4,2]))
rect_up_ovest = T([1,2,3])([1.8,5,3.5])(CUBOID([0,4,2]))
#triangular element of the central structure
rectC = T([1,2,3])([1.8,2,5.5])(CUBOID([3.2,0,0.5]))
ptC = MK([3.5,2,7])
centralFront = JOIN([rectC,ptC])
rect_nord = T([2,3])([10,-0.5])(rectC)

central = COLOR(brown)(STRUCT([a,b,c,d,column_sud_central,column_nord_central,rect_est,rect_ovest,centralFront,rect_up_est,rect_up_ovest,rect_nord]))
vertical_mock_up_3D = STRUCT([columns,front,central])

mock_up_3D = STRUCT([vertical_mock_up_3D,two_and_half_model])

VIEW(mock_up_3D)

