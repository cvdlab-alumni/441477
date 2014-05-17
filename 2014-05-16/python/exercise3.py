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
#from exercise1 import *
from architectural import *


def view_numbered_cells(diagram):
	V,CV = diagram
	hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
	hpc = cellNumbering (diagram,hpc)(range(len(CV)),CYAN,2)
	return VIEW(hpc)

"""merge multiple diagrams in different cells of master.
   To arginate the problem of cells elimination, insert in input diagram whitout cell to eliminate
   e.g. diagram = wall schema whitout the cell corresponding to the door"""

def multiple_diagrams2cells(diagrams,master,toMerge):
	V,CV = master
	for i in range(len(CV))[::-1]:
		if i in toMerge:
			k = toMerge.index(i)
			master = diagram2cell(diagrams[k],master,toMerge[k])
	return master

def remove_cells(master,toRemove):
	return master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


"""
Functions that automatize the loop "merging-numbering-elimination" creating doors and windows:


Functions for the creation of doors in the walls.
	input: door's dimensions, master, numbers of cells where put the doors
	output: master with doors in established walls"""
def doors2x_walls (height,width,master,cells):
    door = assemblyDiagramInit([3,1,2])([[1.5,width,1.5],[0.2],[height,0.5]])
    door = remove_cells( door, [2])
    doors = []
    for i in range(len(cells)):
        doors.append(door)
    master = multiple_diagrams2cells(doors,master,cells)
    return master

def doors2y_walls (height,width,master,cells):
    door = assemblyDiagramInit([1,3,2])([[0.2],[1.5,width,1.5],[height,0.5]])
    door = remove_cells( door, [2])
    doors = []
    for i in range(len(cells)):
        doors.append(door)
    master = multiple_diagrams2cells(doors,master,cells)
    return master
"""
Functions for the creation of window in the walls.
	input: window's dimensions, master, numbers of cells where put the windows
	output: master with window in established walls"""
def windows2x_walls (height,width,master,cells):
    window = assemblyDiagramInit([5,1,3])([[0.2,width,0.5,width,0.2],[0.2],[1,height,0.5]])
    window = remove_cells( window, [4,10])
    windows = []
    for i in range(len(cells)):
        windows.append(window)
    master = multiple_diagrams2cells(windows,master,cells)
    return master

def windows2y_walls (height,width,master,cells):
    window = assemblyDiagramInit([1,5,3])([[0.2],[0.2,width,0.5,width,0.2],[1,height,0.5]])
    window = remove_cells( window, [4,10])
    windows = []
    for i in range(len(cells)):
        windows.append(window)
    master = multiple_diagrams2cells(windows,master,cells)
    return master


DRAW = COMP([VIEW,STRUCT,MKPOLS])


"""test removeCells"""
appartamento = assemblyDiagramInit([5,7,2])([[0.2,3,0.2,5,0.2],[0.2,4,0.2,4,0.2,3,0.2],[0.2,3]])
V,CV = appartamento
toRemove=[17,21,25,35,45,49,53]
appartamento = remove_cells(appartamento,toRemove)
toMerge = 3
ringhiera = assemblyDiagramInit([1,8,3])([[0.2],[0.5,0.4,0.5,0.4,0.5,0.4,0.5,0.4],[1,0.2,1.8]])
appartamento = diagram2cell(ringhiera,appartamento,toMerge)
toRemove = [62,64,67,68,70,73,74,76,79,80,82,85]
appartamento = remove_cells(appartamento, toRemove)

hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
VIEW(hpc)
appartamentoW = appartamento

"""test multiple_diagrams2cells"""
porta = assemblyDiagramInit([3,1,2])([[1.5,2,1.5],[0.2],[2.5,0.5]])
portaY = assemblyDiagramInit([1,3,2])([[0.2],[1.5,2,1.5],[2.5,0.5]])
finestre = assemblyDiagramInit([1,5,3])([[0.2],[0.4,1,0.2,1,0.4],[1.5,0.8,0.7]])
diagrams = [porta,porta,porta,porta,portaY,portaY,finestre,finestre]
appartamento = multiple_diagrams2cells (diagrams,appartamento,[17,41,44,20,27,55,6,10])
hpc = SKEL_1(STRUCT(MKPOLS(appartamento)))
hpc = cellNumbering (appartamento,hpc)(range(len(appartamento[1])),CYAN,2)
VIEW(hpc)


appartamento = remove_cells(appartamento, [69,75,81,87,93,101,107,116,122])


"""test doors2_walls"""
DRAW(appartamentoW)
appartamentoW = doors2x_walls (2.5,2,appartamentoW,[17,20,41,44])
appartamentoW = doors2y_walls (2.5,2,appartamentoW,[25,51])
DRAW(appartamentoW)
"""test windows2x_walls"""
appartamentoW = windows2y_walls(0.8,0.8,appartamentoW,[6,10])
DRAW(appartamentoW)