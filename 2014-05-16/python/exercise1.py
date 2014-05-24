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

def multipleMerge(diagram,master,toMerge):
	for cella in toMerge:
		master = diagram2cell(diagram,master,cella)
	return master
def colorRGB(values):
      	return COLOR([ values[0]/255.0,
                         values[1]/255.0,
                         values[2]/255.0])

#funziona per colorare alcune celle del master
def colorLarElements(color, master,element):
	for i in element:
		master[i]=COLOR(color)(master[i])
	return master
#funzioni che rende trasparenti le celle del master
def transparentLarElements(master,element):
	for i in element:
		master[i]=MATERIAL([1,1,1,0, 0,0,0,0.3, 0,0,0,0, 0,0,0,0, 40])(master[i])
	return master
#funzione che apllica la texture alle celle indicate
def textureLarElements(master,element,texture):
	for i in element:
		master[i]=TEXTURE(texture)(master[i])
	return master


DRAW = COMP([VIEW,STRUCT,MKPOLS])

appartamento = assemblyDiagramInit([5,7,2])([[0.2,3,0.2,5,0.2],[0.2,4,0.2,4,0.2,3,0.2],[0.2,3]])


V,CV = appartamento
hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove=[17,21,25,35,45,49,53]
appartamento = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(appartamento)

hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
#VIEW(hpc)

toMerge = 3
ringhiera = assemblyDiagramInit([1,8,3])([[0.2],[0.5,0.4,0.5,0.4,0.5,0.4,0.5,0.4],[1,0.2,1.8]])
appartamento = diagram2cell(ringhiera,appartamento,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
#VIEW(hpc)

toRemove = [62,64,67,68,70,73,74,76,79,80,82,85]
appartamento = appartamento[0], [cell for k,cell in enumerate(appartamento[1]) if not (k in toRemove)]
#DRAW(appartamento)

hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
#VIEW(hpc)

toMerge = [20,40,42]
porta = assemblyDiagramInit([3,1,2])([[1.5,2,1.5],[0.2],[2.5,0.5]])
appartamento = multipleMerge(porta,appartamento,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
#VIEW(hpc)
#
#portaDettagliata = assemblyDiagramInit([5,3,3])([[0.2,0.7,0.2,0.7,0.2],[0.05,0.1,0.05],[0.2,2.1,0.2]])#
#appartamento = diagram2cell(portaDettagliata,appartamento,85)#
#appartamento = diagram2cell(portaDettagliata,appartamento,79)#
#appartamento = diagram2cell(portaDettagliata,appartamento,73)


#toRemove = [141,147,165,159,96,114,102,120,204,210,192,185]

#appartamento = appartamento[0], [cell for k,cell in enumerate(appartamento[1]) if not (k in toRemove)]


finestra = assemblyDiagramInit([1,3,3])([[0.2],[0.5,2,0.5],[1.5,1,0.5]])
finestraDettagliata = assemblyDiagramInit([1,3,3])([[0.2],[0.2,1.6,0.2],[0.2,0.6,0.2]])
appartamento = diagram2cell(finestra,appartamento,10)
hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,.6)
#VIEW(hpc)
appartamento = diagram2cell(finestraDettagliata,appartamento,92)

portaBalcone = assemblyDiagramInit([1,3,2])([[0.2],[1.5,1,1.5],[2,1]])
portaIngresso = assemblyDiagramInit([1,3,2])([[0.2],[1.25,1.5,1.25],[2,.5]])

appartamento = diagram2cell(portaBalcone,appartamento,25)
appartamento = diagram2cell(portaIngresso,appartamento,50)
hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,.6)
#VIEW(hpc)
#DRAW(appartamento)

appartamentoHPC = MKPOLS(appartamento)
"""elementi trasparenti"""
appartamentoHPC = transparentLarElements(appartamentoHPC,[6,16,98,103,104,106,107,108])
"""legno finestra"""
appartamentoHPC = textureLarElements(appartamentoHPC,[94,95,96,97,99,100,101,102],'../images/legno.jpg')
appartamentoHPC = textureLarElements(appartamentoHPC,[105],'../images/tendina.jpg')
appartamentoHPC = textureLarElements(appartamentoHPC,[0,1,2,3,4,5,7,8,9,10,11,13,12,20,21,22,23,26,32,33,34,35,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,86,87,88,89,90,91,92,93,109,110,112,113,114],'../images/pietra.jpg')
appartamentoHPC = textureLarElements(appartamentoHPC,[70,76,82,111],'../images/legno.jpg')
appartamentoHPC = textureLarElements(appartamentoHPC,[17,19,27,36,38,40],'../images/pavimento.jpg')
appartamentoHPC = textureLarElements(appartamentoHPC,[14],'../images/pavimentoEsterno.jpg')
#appartamento = colorLarElements([153,204,255],appartamento,[85,96,97,98,100,101,102,103])
VIEW(STRUCT(appartamentoHPC))
