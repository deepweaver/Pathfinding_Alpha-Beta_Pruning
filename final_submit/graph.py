'''
CISC 352 - Assignment 2 - Pathfinding - pathfinding
Written by: Group 13
Date last editted: March. 11, 2019

This program has four modules, and an additional experiment module that
is only used to compile data on the performance of the two algorithms.

Main - pathfinding.py
fileIO.py
findpath.py
[ graph.py ]
experiment.py

This module encapsulates the Graph object.
'''

class Graph:
    '''
    The constructor of the Graph object,
    defines the map, start and goal attributes
    '''
    def __init__(self, grids):
        m = []
        for line in grids:
            m.append(line)
        self.map = m
        self.findSG(grids)

    '''
    This function identifies the indices of the start point
    and the goal state of the given input grid, and store them as tuples
    in the start and goal attributes.
    '''
    def findSG(self,grids):
        for y in range(len(grids)):
            if 'S' in grids[y]:
                #print("found start")
                x = grids[y].index('S')
                self.start = (y,x)
            if 'G' in grids[y]:
                #print("found goal")
                x = grids[y].index('G')
                self.goal = (y,x)


    '''
    This function takes the current node as argument
    finds all the neighboring nodes and add to a list
    (only up, down, left, right neighbors)
    returns this neighbor node list 
    '''
    def neighbor(self, current):
        grids = self.map
        neighbors = []
        accepted = ['G', '_']
        range0 = len(grids)
        range1 = len(grids[0])
        top = (current[0]-1, current[1])
        bottom = (current[0]+1, current[1])
        left = (current[0], current[1]-1)
        right = (current[0], current[1]+1)
        
        if top[0] in range(range0) and top[1] in range(range1):
            if grids[top[0]][top[1]] in accepted:
                neighbors.append(top)
        if bottom[0] in range(range0) and bottom[1] in range(range1):
            if grids[bottom[0]][bottom[1]] in accepted:
                neighbors.append(bottom)
        if left[0] in range(range0) and left[1] in range(range1):
            if grids[left[0]][left[1]] in accepted:
                neighbors.append(left)
        if right[0] in range(range0) and right[1] in range(range1):
            if grids[right[0]][right[1]] in accepted:
                neighbors.append(right)

        return neighbors


    '''
    This function takes the current node as argument,
    finds all neighboring nodes including up, down, left,
    right, and diagonal neighbors.
    Returns all the neighboring nodes in a list 
    '''
    def diagNeighbor(self, current):
        grids = self.map
        diagNei = self.neighbor(current)
        accepted = ['G', '_']
        range0 = len(grids)
        range1 = len(grids[0])
        bottomRight = (current[0]+1, current[1]+1)
        bottomLeft = (current[0]+1, current[1]-1)
        topRight = (current[0]-1, current[1]+1)
        topLeft = (current[0]-1, current[1]-1)
        
        if bottomRight[0] in range(range0) and bottomRight[1] in range(range1):
            if grids[bottomRight[0]][bottomRight[1]] in accepted:
                diagNei.append(bottomRight)
        if bottomLeft[0] in range(range0) and bottomLeft[1] in range(range1):
            if grids[bottomLeft[0]][bottomLeft[1]] in accepted:
                diagNei.append(bottomLeft)
        if topRight[0] in range(range0) and topRight[1] in range(range1):
            if grids[topRight[0]][topRight[1]] in accepted:
                diagNei.append(topRight)
        if topLeft[0] in range(range0) and topLeft[1] in range(range1):
            if grids[topLeft[0]][topLeft[1]] in accepted:
                diagNei.append(topLeft)

        return diagNei


    # This function is written for easier debugging process
    # it pretty prints the graph
    def printGraph(self):
        for line in self.map:
            print(line)

        
#test
if __name__ == "__main__":
    grids = ['XXXXXXXXXX',
             'X___XX_X_X',
             'X_X__X___X',
             'XSXX___X_X',
             'X_X__X___X',
             'X___XX_X_X',
             'X_X__X_X_X',
             'X__G_X___X',
             'XXXXXXXXXX']
    g1 = Graph(grids)
    print(g1.map)
    print(g1.start)
    print(g1.goal)
    print(g1.neighbor([6,4]))
    print(g1.diagNeighbor([6,4]))
    g1.printGraph()
    
