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
toRemove = [79,85,73]
appartamento = appartamento[0], [cell for k,cell in enumerate(appartamento[1]) if not (k in toRemove)]
#DRAW(appartamento)

toMerge = 26
porta = assemblyDiagramInit([1,3,2])([[0.2],[1.5,2,1.5],[2.5,0.5]])
appartamento = diagram2cell(porta,appartamento,toMerge)


toRemove = [87]
appartamento = appartamento[0], [cell for k,cell in enumerate(appartamento[1]) if not (k in toRemove)]
finestre = assemblyDiagramInit([1,5,3])([[0.2],[0.4,1,0.2,1,0.4],[1.5,0.8,0.7]])
appartamento = diagram2cell(finestre,appartamento,6)
appartamento = diagram2cell(finestre,appartamento,9)

toRemove = [92,98,107,113]
appartamento = appartamento[0], [cell for k,cell in enumerate(appartamento[1]) if not (k in toRemove)]

toMerge = 49
porta = assemblyDiagramInit([1,3,2])([[0.2],[1.5,2,1.5],[2.5,0.5]])
appartamento = diagram2cell(porta,appartamento,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
#VIEW(hpc)

toRemove = [115]
appartamento = appartamento[0], [cell for k,cell in enumerate(appartamento[1]) if not (k in toRemove)]

hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
#VIEW(hpc)
DRAW(appartamento)

