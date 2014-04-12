# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:31:05 2014

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
import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, '/home/chiara/lar-cc/lib/py/')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *



#function to define color
def colorRGB(values):
        return Color4f([ values[0]/255.0,
                         values[1]/255.0,
                         values[2]/255.0,
                         1.0])
                
green = colorRGB([0,153,0])
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
vertical_mock_up_3D = STRUCT([columns,front,central,back,decorations])
solid_model_3D = STRUCT([two_and_half_model,vertical_mock_up_3D,stairs,central])
#mountaion
mount = checkModel(larTorus([8,7])())
mountain = T([1,2,3])([4,6,-9])(STRUCT(MKPOLS(mount)))
base = larPizza([8,25])([8,30])
baseStruct = T([1,2,3])([4,6,-19])(STRUCT(MKPOLS(base)))
townUp = T([1,2,3])([4,6,-20])(STRUCT(MKPOLS(base)))
townDown=T([1,2,3])([-75,-75,-30])(CUBOID([150,150,10]))
town= COLOR(green)(JOIN([townUp,townDown]))
baseMountain = COLOR(green)(JOIN([mountain,baseStruct]))
#albero
tronco=COLOR(colorRGB([52,25,0]))(CYLINDER([0.25,1.7])(32))
sfera=T([3])([1.7])(STRUCT(MKPOLS(larBall(1)([15,36]))))
pt=MK([0,0,4])
chioma=COLOR(colorRGB([0,102,0]))(JOIN([sfera,pt]))
albero=STRUCT([tronco,chioma])
a=T([1,2,3])([-11.5,34,-12.6])(STRUCT(NN(4)([T(1)(2),albero])))
b=T([1,2,3])([-11.5,33,-12.6])(albero)
a2=T([1,2,3])([-5,37,-13])(STRUCT(NN(4)([T(1)(1.5),albero])))
a3=T([1,2,3])([1.5,36,-13])(STRUCT(NN(6)([T(1)(2.2),albero])))
#alberi sx
a4=T([1,2,3])([-26,-7,-13])(R([1,2])(PI/2)(STRUCT(NN(10)([T(1)(2.5),albero]))))
b1=T([1,2,3])([-23,15,-13])(R([1,2])(PI/2)(STRUCT(NN(2)([T(1)(2.5),albero]))))
b2=T([1,2,3])([-13,30,-12.6])(albero)
b3=T([1,2,3])([-15,28,-12.6])(albero)
b4=T([1,2,3])([-17,26,-12.6])(albero)
b5=T([1,2,3])([-19,24,-12.6])(albero)
b7=T([1,2,3])([-21,22,-12.6])(albero)
angolo1=STRUCT([b2,b3,b4,b5,b7])
b6=T([1,2,3])([17,32,-12.6])(albero)
b8=T([1,2,3])([15,34,-12.6])(albero)
#alberi dx
angolo4=T([1,2])([45,-37,-12.6])(angolo1)
angolo5=T([1,2])([35,-47,-12.6])(angolo1)
angolo2=T([1,2])([10,1])(R([1,2])(PI/2)(angolo1))
angolo3=T([1,2])([52,43])(R([1,2])(PI/2)(angolo1))
a5=T([1,2,3])([35,1,-13])(R([1,2])(PI/2)(STRUCT(NN(5)([T(1)(2.5),albero]))))
a6=T([1,2,3])([33,-5,-13])(R([1,2])(PI/2)(STRUCT(NN(6)([T(1)(1.5),albero]))))
a7=T([1,2,3])([33,5,-13])(R([1,2])(PI/2)(STRUCT(NN(6)([T(1)(2.3),albero]))))
alberi=STRUCT([a,b,a2,a3,a4,a5,a6,a7,b1,b6,b8,angolo1,angolo2,angolo3,angolo4,angolo5])
#tempietto
tempietto=T([1,2,3])([-35,40,-16.5])(S([1,2,3])([0.5,0.5])(STRUCT([two_and_half_model,columns,front,decoration])))
colonne_a_terra1=T([1,2,3])([-35,55,-16])(R([1,3])(PI/2)((CYLINDER([0.15,4])(32))))
colonne_a_terra2=T([1,2,3])([-35,54.5,-16])(R([1,3])(PI/2)((CYLINDER([0.15,4])(32))))
colonne_a_terra3=T([1,2,3])([-36,52,-15.9])(R([2,3])(-PI/2)((CYLINDER([0.15,4])(32))))
colonne_a_terra=COLOR(colorFloor2)(STRUCT([colonne_a_terra1,colonne_a_terra2,colonne_a_terra3]))
#rovine
rect2=T([1,2,3])([0.25,12.75,5.7])(CUBOID([6.5,1,1]))
ptCol=MK([3.5,13,8])
triCol=JOIN([rect2,ptCol])
rovine=COLOR(colorRGB([203,154,54]))(T([1,2,3])([-15,25,-14])(S(3)(0.7)(STRUCT([columns_sud,triCol]))))
colonneRovina=T([1,2,3])([11,-19,3.5])(S([1,2,3])(0.7)((STRUCT([colonne_a_terra1,colonne_a_terra2]))))
centralRovine=T([1,2,3])([-22,40,-14.5])(S([1,2,3])([0.4,0.3,0.4])((central)))
rovine2=T([1,2,3])([-19,28,-11])(S([1,2,3])([0.5,0.5,0.3])(rovine))
rovine3=T([1,2,3])([-15,25,-31.8])(R([2,3])(PI/2)(S([1,2,3])([0.5,0.5,0.3])(rovine)))
colonnato=COLOR(colorRGB([203,154,54]))(T([1,2,3])([-14,39,-15.7])(S([1,2,3])([0.7,0.7,0.9])((STRUCT([columns_est,columns_ovest])))))
valleRovine=STRUCT([rovine,colonneRovina,centralRovine,rovine2,rovine3,colonnato])
#tempio2,altre rovine
cubo_a=CUBOID([4,4,0.5])
cubo_b=T([1,2,3])([0.5,0.5,0.5])(CUBOID([3,3,0.5]))
cubo_c=T([1,2,3])([1,1,1])(CUBOID([2,2,.5]))
base_tempio2=STRUCT([cubo_a,cubo_b,cubo_c])
colonne_tempio2=T([1,2,3])([0.5,1.5,1.5])(STRUCT(NN(2)([T(1)(1),CYLINDER([0.25,3.5])(32)])))
rect_tempio2=T([1,2,3])([1,1.25,5])(CUBOID([2,0.5,1]))
tempio2=COLOR(colorRGB([51,51,0]))(T([1,2,3])([-20,50,-16])(STRUCT([base_tempio2,colonne_tempio2,rect_tempio2])))
final=STRUCT([baseMountain,solid_model_3D,town,alberi,tempietto,colonne_a_terra,valleRovine,tempio2])
VIEW(final)
