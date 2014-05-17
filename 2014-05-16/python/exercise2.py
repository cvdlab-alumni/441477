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

from sysml import *
from exercise1 import *
from architectural import *


dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])

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

condominio = assemblyDiagramInit([3,2,4])([[8.6,3,8.6],2*[11.8],4*[3.2]])

V,CV = condominio
hpc = SKEL_1(STRUCT(MKPOLS(condominio)))
hpc = cellNumbering (condominio,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
condominio = diagram2cell(appartamento,condominio,0)
hpc = SKEL_1(STRUCT(MKPOLS(condominio)))
hpc = cellNumbering (condominio,hpc)(range(len(condominio[1])),CYAN,2)
#VIEW(hpc)
#DRAW(condominio)
condominio = diagram2cell(appartamento,condominio,1)
condominio = diagram2cell(appartamento,condominio,0)
condominio = diagram2cell(appartamento,condominio,1)
condominio = diagram2cell(appartamento,condominio,1)
condominio = diagram2cell(appartamento,condominio,0)
condominio = diagram2cell(appartamento,condominio,0)
condominio = diagram2cell(appartamento,condominio,0)

appartamentoR = larApply(r(0,0,PI))(appartamento)
condominio = diagram2cell(appartamentoR,condominio,8)
condominio = diagram2cell(appartamentoR,condominio,8)
condominio = diagram2cell(appartamentoR,condominio,8)
condominio = diagram2cell(appartamentoR,condominio,8)
condominio = diagram2cell(appartamentoR,condominio,8)
condominio = diagram2cell(appartamentoR,condominio,8)
condominio = diagram2cell(appartamentoR,condominio,8)
condominio = diagram2cell(appartamentoR,condominio,8)

stair = spiralStair(width=0.1,R=2,r=0.1,riser=0.1,pitch=4,nturns=3,steps=36)
stair = larApply(t(10,26,0))(stair)

pianerottolo = assemblyDiagramInit([1,1,2])([[1],[1],[0.1,1]])
condominio = diagram2cell(pianerottolo,condominio,0)
condominio = diagram2cell(pianerottolo,condominio,0)
condominio = diagram2cell(pianerottolo,condominio,0)
condominio = diagram2cell(pianerottolo,condominio,0)
condominio = diagram2cell(pianerottolo,condominio,0)
condominio = diagram2cell(pianerottolo,condominio,0)
condominio = diagram2cell(pianerottolo,condominio,0)
condominio = diagram2cell(pianerottolo,condominio,0)

hpc = SKEL_1(STRUCT(MKPOLS(condominio)))
hpc = cellNumbering (condominio,hpc)(range(len(condominio[1])),CYAN,2)
#VIEW(hpc)

toRemove = [1889,1891,1893,1895,1897,1899,1901,1903]
condominio = condominio[0], [cell for k,cell in enumerate(condominio[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(condominio)))
hpc = cellNumbering (condominio,hpc)(range(len(condominio[1])),CYAN,2)
#VIEW(hpc)
#DRAW(condominio)

#condominioStruct = COLOR(colorRGB([255,255,102]))(STRUCT(MKPOLS(condominio)))
tetto = COLOR(colorRGB([165,42,42]))(T(3)(12.8)(JOIN([CUBOID([20.2,23.6,1]),MK([10.1,11.8,8])])))
pavimento = COLOR(colorRGB([50,205,50]))(T([1,2,3])([-8,-15,-1])(CUBOID([40,60,1])))


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
macchina = T(2)(33)(S([1,2,3])([0.3,0.3,0.3])(R([2,3])(PI/2)(STRUCT([ruote,struttura]))))

finestrinoAB=COLOR(colorRGB([218,253,218]))(T(3)(-0.1)(PROD([finestrinoApiatto,Q(0.3)])))
finestrinoBB=T(3)(3.45)(finestrinoAB)
strutturaB=COLOR(BLUE)(PROD([profilo1,Q(3.5)]))
strutturaB=STRUCT([strutturaB,finestrinoAB,finestrinoBB])
macchinaB = T(2)(31)(S([1,2,3])([0.3,0.3,0.3])(R([2,3])(PI/2)(STRUCT([ruote,strutturaB]))))

"""quadro completo"""
assembly3D = evalStruct(Struct([stair,t(0,0,4)]*2))
baseCasa = STRUCT(CAT(AA(MKPOLS)(assembly3D)) + MKPOLS(condominio))
pianoScala1 = T([1,2,3])([8.1,23,0.1])(CUBOID([4,3,0.2]))
pianoScala2 = T([1,2,3])([8.6,23,3.3])(CUBOID([3,1.5,0.2]))
pianoScala3 = T(3)(3.2)(pianoScala2)
pianoScala4 = T(3)(9.6)(pianoScala1)
pianoScala = STRUCT([pianoScala1,pianoScala2,pianoScala3,pianoScala4])
condominioStruct = COLOR(colorRGB([255,255,102]))(STRUCT([baseCasa,pianoScala]))

VIEW(STRUCT([pavimento,condominioStruct,tetto,macchina,macchinaB]))