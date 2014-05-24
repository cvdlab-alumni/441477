from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, '/home/chiara/lar-cc/lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from architectural import *
from sysml import *
from exercise1 import *

def bez(points):
    return BEZIER(S1)(points)
    
def map1D(controlpoints):
    return MAP(BEZIER(S1)(controlpoints))(dom1D)
    
def map2D(functions):
	return MAP(BEZIER(S2)(functions))(dom2D)

def colorRGB(values):
        return Color4f([ values[0]/255.0,
                         values[1]/255.0,
                         values[2]/255.0,
                         1.0])

dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])

condominio = assemblyDiagramInit([3,2,4])([[8.6,3,0.2],2*[11.8],[0.2,3.2,0.2,3.2]])
bucoScala = assemblyDiagramInit([1,2,1])([[3],[2,9.8],[0.2]])


V,CV = condominio

toRemove = [9,11,13,15]
condominio = condominio[0], [cell for k,cell in enumerate(condominio[1]) if not (k in toRemove)]
condominio = diagram2cell(bucoScala,condominio,11)
toRemove = [19]
condominio = condominio[0], [cell for k,cell in enumerate(condominio[1]) if not (k in toRemove)]


condominio = diagram2cell(appartamento,condominio,7)
condominio = diagram2cell(appartamento,condominio,5)
condominio = diagram2cell(appartamento,condominio,3)
condominio = diagram2cell(appartamento,condominio,1)

hpc = SKEL_1(STRUCT(MKPOLS(condominio)))
hpc = cellNumbering (condominio,hpc)(range(len(condominio[1])),CYAN,2)
#VIEW(hpc)

"""scala"""
stair = spiralStair(width=0.5,R=1.6,r=0.1,riser=0.2,pitch=6.2,nturns=1,steps=30)
stair = larApply(t(10.2,11.8,0))(stair)
stair2 = larApply(r(0,0,PI))(larApply(t(-20.4,-23.9,3.4))(stair))
stair = TEXTURE('../images/legno.jpg')(STRUCT(MKPOLS(stair)+MKPOLS(stair2)))
pianerottolo = T([1,2,3])([10.2,11.8,3.4])(CUBOID([1.5,2,0.2]))
pianerottolo2 = TEXTURE('../images/legno.jpg')(T(3)(3.3)(pianerottolo))
pianerottolo3 = T(3)(0.2)(pianerottolo2)



condominio = MKPOLS(condominio)
condominio = transparentLarElements(condominio,[12,8,22,32,229,114,137,147,123,124,122,120,119,238,234,239,237,235,252,367,262,377,349,350,352,353,354,464,465,467,468,469,344,459,229,114])
condominio = textureLarElements(condominio,[121,236,351,466],'../images/tendina.jpg')
condominio = textureLarElements(condominio,[340,341,342,343,345,346,347,348,455,456,457,458,460,461,462,463,225,226,227,228,230,231,232,233,110,111,112,113,115,116,117,118],'legno.jpg')
condominio = textureLarElements(condominio,[316,328,357,322,431,443,437,201,213,207,98,92,86,127,357,242,472],'../images/legno.jpg')
condominio = textureLarElements(condominio,[273,388,43,158,54,56,35,33,52,286,265,284,263,282,397,399,378,380,401,167,145,169,148,171,150],'pavimento.jpg')
condominio = textureLarElements(condominio,[30,260,375,30,145],'../images/pavimentoEsterno.jpg')
condominio = textureLarElements(condominio,[19,21,136,366,251,164,25,23,26,20,16,256,254,253,368,369,106,336,453,448,449,332,257,372,132,17,417,418,419,420,421,422,423,424,425,426,427,428,247,248,280,154,185,172,153,151,141,222,140,220,138,217,139,219,221,224,102,105,24,139,72,73,74,75,76,77,78,80,39,279,394,154,255,270,18,366,364,268,370,365,387,363,272,258,220,289,268,246,259,290,384,362,361,373,383,395,404,405,10,14,187,188,189,190,191,192,193,194,195,196,197,198,135,152,133,134,135,371,370,372,337,338,339,333,334,335,450,447,452,449,451,454,250,365,302,303,304,305,306,307,308,309,310,311,312,313,272,259,281,269,258,374,384,396,71,70,57,58,48,49,36,37,186,173,154,185,172,154,153,152,151,142,27,107,108,109,105,102,103,104,222,223,217,218,219,82,83,81,79],'../images/pietra.jpg')
condominio = STRUCT(condominio)

tettoA = CUBOID([16,26,1.5])
tettoB = T([1,2,3])([0.2,0.2,0.2])(CUBOID([15.6,25.6,1.4]))
tetto = T([1,2,3])([-2,-1.3,6.8])(DIFFERENCE([tettoA,tettoB]))
ringhiera = T([1,2,3])([8.8,23.2,3.4])(TEXTURE('../images/legno.jpg')(STRUCT(NN(8)([ CUBOID([.2,0.2,1.5]) ,T(1)(0.4)]))))
ringhieraA = T(2)(-23)(ringhiera)

"""esterno"""
pavimento = T([1,2,3])([-2,-1,-0.5])(CUBOID([40,25,0.5]))
lago =  MATERIAL([1,1,2,0.1, 0,1,0.8,0.5, 1,1,0,0.1, 1,0,1,0.1, 30])(T([1,2,3])([-12,-1,-0.5])(CUBOID([10,25,0.3])))
acqua = COLOR(BLUE)(T([1,2,3])([-12,-1,-0.6])(CUBOID([10,25,0.1])))
lago = STRUCT([lago,acqua])
strada = TEXTURE('../images/strada.jpg')(T([1,2,3])([35,-1,-0.5])(CUBOID([5,25,0.6])))
prato = TEXTURE('../images/prato.jpg')(T([1,2])([-2,-1])(CUBOID([36,25,0.1])))
campo = TEXTURE('../images/campo.jpg')(T([1,2])([20,-1])(CUBOID([11,25,0.2])))
"""alberi"""
#albero
tronco=COLOR(colorRGB([52,25,0]))(CYLINDER([0.25,1.7])(32))
sfera=T([3])([1.7])(STRUCT(MKPOLS(larBall(1)([15,36]))))
pt=MK([0,0,4])
chioma=COLOR(colorRGB([0,102,0]))(JOIN([sfera,pt]))
albero=STRUCT([tronco,chioma])
alberi2 = T([1])([34])(STRUCT(NN(14)([albero,T(2)(1.8)])))

prato = STRUCT([prato,campo,alberi2])

""" Elementi curvi: macchine rappresentate con curve di BEZIER """
#1D
b1 = map1D([[0.14, 1.16], [0.07, 2.26], [0.05, 3.03], [2.37, 3.49]])
b2 = map1D([[2.37, 3.49], [2.71, 3.11], [5.01, 5.12], [7.23, 4.97]])
b3 = map1D([[7.23, 4.97], [9.22, 4.93], [9.67, 4.07], [10.45, 3.82]])
b4 = map1D([[10.45, 3.82], [12.42, 3.68], [12.78, 3.79], [12.72, 1.22]])
b5 = map1D([[12.72, 1.22], [12.54, 1.14], [12.42, 0.94], [12.04, 1.01]])
b6 = map1D([[12.04, 1.01], [11.92, 2.91], [9.53, 2.62], [9.73, 0.91]])
b7 = map1D([[3.86, 0.95], [6.77, 0.91], [7.4, 0.91], [9.73, 0.91]])
b8 = map1D([[3.86, 0.95], [3.91, 2.71], [1.45, 2.91], [1.52, 0.83]])
b9 = map1D([[0.14, 1.16], [0.1, 0.86], [0.74, 0.97], [1.52, 0.83]])
finestrino1=map1D([[3.35, 3.3], [3.91, 3.83], [5.65, 4.76], [6.61, 4.76]])
finestrino2=map1D([[6.61, 4.76], [8.25, 4.88], [9.03, 4.31], [9.48, 3.65]])
finestrino3=map1D([[9.48, 3.65], [8.54, 3.55], [8.25, 3.49], [3.35, 3.3]])
finestrino=STRUCT([finestrino1,finestrino2,finestrino3])
finestrinoApiatto=SOLIDIFY(finestrino)
finestrinoA=COLOR(BLUE)(T(3)(-0.1)(PROD([finestrinoApiatto,Q(0.3)])))
finestrinoB=T(3)(3.45)(finestrinoA)
profilo = STRUCT([b1,b2,b3,b4,b5,b6,b7,b8,b9])
profilo1=SOLIDIFY(profilo)
ruota=CYLINDER([1.1,0.8])(32)
ruota1=T([1,2,3])([2.65,1.1,-0.4])(ruota)
ruota3=T(3)(3.5)(ruota1)
ruota2=T([1])(8.25)(ruota1)
ruota4=T(3)(3.5)(ruota2)
ruote=COLOR(BLACK)(STRUCT([ruota1,ruota2,ruota3,ruota4]))
struttura=COLOR(RED)(PROD([profilo1,Q(3.5)]))
struttura=STRUCT([struttura,finestrinoA,finestrinoB])
macchina = T([1,2])([36,10])(R([1,2])(PI/2)(S([1,2,3])([0.2,0.2,0.2])(R([2,3])(PI/2)(STRUCT([ruote,struttura])))))
finestrinoAB=COLOR(colorRGB([218,253,218]))(T(3)(-0.1)(PROD([finestrinoApiatto,Q(0.3)])))
finestrinoBB=T(3)(3.45)(finestrinoAB)
strutturaB=COLOR(BLUE)(PROD([profilo1,Q(3.5)]))
strutturaB=STRUCT([strutturaB,finestrinoAB,finestrinoBB])
macchinaB = T([1,2])([39,5])(R([1,2])(3*PI/2)(S([1,2,3])([0.2,0.2,0.2])(R([2,3])(PI/2)(STRUCT([ruote,strutturaB])))))


VIEW(STRUCT([condominio,stair,pianerottolo,pianerottolo2,pianerottolo3,pavimento,lago,tetto,strada,macchina,macchinaB,prato,ringhiera,ringhieraA]))
