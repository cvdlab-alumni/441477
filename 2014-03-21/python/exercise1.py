# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 02:30:32 2014

@author: chiara
"""

from pyplasm import *

#function to define color

def colorRGB(values):
        return Color4f([ values[0]/255.0,
                         values[1]/255.0,
                         values[2]/255.0,
                         1.0])
                
green = colorRGB([60,179,113])
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
VIEW(two_and_half_model)