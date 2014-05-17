

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


def view_numbered_cells(diagram):
    V,CV = diagram
    hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
    hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
    return VIEW(hpc)


def new_diagram2cell(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)
   V1,CV1 = master
   CV1 = [c for k,c in enumerate(CV1) if k != cell]
   V,CV1,CV2,n12 = vertexSieve((V1,CV1),diagram)
   """
   # yet to finish coding
   masterBoundaryFaces = boundaryOfChain(CV,FV)([cell])
   diagramBoundaryFaces = lar2boundaryFaces(CV,FV)
   """
   CV = CV1+CV2
   master = V, CV
   return master


"""Test"""

appartamento = assemblyDiagramInit([5,7,2])([[0.2,3,0.2,5,0.2],[0.2,4,0.2,4,0.2,3,0.2],[0.2,3]])
V,CV = appartamento
toRemove=[17,21,25,35,45,49,53]
appartamento = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

toMerge = 3
ringhiera = assemblyDiagramInit([1,8,3])([[0.2],[0.5,0.4,0.5,0.4,0.5,0.4,0.5,0.4],[1,0.2,1.8]])
appartamento1 = diagram2cell(ringhiera,appartamento,toMerge)
print len(appartamento1[0])
#view_numbered_cells(appartamento1)

new_appartamento = new_diagram2cell(ringhiera,appartamento,toMerge)
print len(new_appartamento[0])
#view_numbered_cells(new_appartamento)
