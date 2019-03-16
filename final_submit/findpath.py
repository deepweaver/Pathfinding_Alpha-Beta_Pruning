'''
CISC 352 - Assignment 2 - Pathfinding - pathfinding
Written by: Group 13
Date last editted: March. 11, 2019

This program performs pathfinding on an m*n grid map using two algorithms:
1) A*
2) Greedy
There are two mode for the pathfinding:
0 - where it can only move in up, down, left and right four directions,
    in this mode Manhattan distance is used as heuristics in calculation.
1 - where it can move to all neighbouring grid including those in diagnals,
    in this mode Chebyshev is used as heuristics.

This program has four modules, and an additional experiment module that
is only used to compile data on the performance of the two algorithms.

Main - pathfinding.py
fileIO.py
[ findpath.py ]
graph.py
experiment.py

This module contains all the functions to find the path between start and goal
'''

import graph
import queue
import random
import time


'''
This function is the heuristic function based on Manhattan distance,
it calculates the distance between the goal and the node it can move from
the current node.

@param goal contains a tuple representing the index of the goal node
@param nextG contains a tuple representing the index of the concerning node

@return heuristics value for this node
'''
def manhattan(goal, nextG):
    startx, starty = nextG[0], nextG[1]
    endx, endy = goal[0], goal[1]

    # manhattan distance = delta(x) + delta(y)
    distanceX = abs(startx - endx)
    distanceY = abs(starty - endy)
    return distanceX + distanceY

'''
This function is the heuristic function based on Chebyshev distance.

@param goal contains a tuple representing the index of the goal node
@param nextG contains a tuple representing the index of the concerning node

@return heuristics value for this node
'''
def chebyshev(goal, nextG):
    startx, starty = nextG[0], nextG[1]
    endx, endy = goal[0], goal[1]

    # chebyshev distance = max( delta(x), delta(y) )
    distanceX = abs(startx - endx)
    distanceY = abs(starty - endy)
    return max(distanceX, distanceY)


'''
This function finds the path between start and goal nodes using A* algorithm.
A priority queue is used to hold the nodes to be explored
Dictionaries are used to store information of the nodes we have explored

@param thisGraph contains the graph object to be solved
@param mode is one of (0,1), in which 0 is the mode where it can only move in 4 directions
       and 1 means it can move in all directions
@return result - a list of strings containing the solution to the input graph
                 where if a path exist, the path will be filled with P between S and G,
                 if the path does not exist, the original graph will be returned
        found - boolean indicating whether a path is found between S and G
        steps - integer value of number of steps to reach the goal from the start,
                i.e. in ['SPPPG'] the step count will be 4
'''
def aStar(thisGraph, mode):
    grids = thisGraph.map               # the list of strings representing the graph
    start = thisGraph.start
    goal = thisGraph.goal
    frontier = queue.PriorityQueue()    # priority queue for the nodes to be explored
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    found = False       # found flag set to be false

    # loops until the goal is found or until the frontier queue is empty
    while not frontier.empty():
        currentG = frontier.get()
        current = currentG[1]

        # exits loop if goal is found, set found flag to true
        if current == goal:
            found = True
            break

        # select mode: 0 - can only move in up, down, left, right;
        #              1 - can move to all neighbouring nodes including in diagonals
        if mode == 0:

            # at mode 0, calls the neighbor function to get the reachable nodes
            for nextG in thisGraph.neighbor(current):
                new_cost = cost_so_far[current] + 1    # the cost for each step is 1
                if nextG not in cost_so_far or new_cost < cost_so_far[nextG]:
                    cost_so_far[nextG] = new_cost
                    priority = new_cost + manhattan(goal, nextG)
                    frontier.put((priority, nextG))
                    came_from[nextG] = current

        elif mode == 1:

            # at mode 1, calls the diagNeighbor function to get the reachable nodes
            for nextG in thisGraph.diagNeighbor(current):
                new_cost = cost_so_far[current] + 1
                if nextG not in cost_so_far or new_cost < cost_so_far[nextG]:
                    cost_so_far[nextG] = new_cost
                    priority = new_cost + chebyshev(goal, nextG)
                    frontier.put((priority, nextG))
                    came_from[nextG] = current

    # checks found flag, if true, calls makePath function to fill in the P for the path
    # if false, the result graph will be the original graph, step count set to 0
    if found:
        result, steps = makePath(came_from, start, goal,grids.copy())
    else:
        result = grids
        steps = 0
    
    return result, found, steps
   

'''
This function finds the path between start and goal nodes using greedy algorithm.
A priority queue is used to hold the nodes to be explored
Dictionaries are used to store information of the nodes we have explored
It's similar to the aStar but we don't concern about the cost_so_far

@param thisGraph contains the graph object to be solved
@param mode is one of (0,1), in which 0 is the mode where it can only move in 4 directions
       and 1 means it can move in all directions
@return result - a list of strings containing the solution to the input graph
                 where if a path exist, the path will be filled with P between S and G,
                 if the path does not exist, the original graph will be returned
        found - boolean indicating whether a path is found between S and G
        steps - integer value of number of steps to reach the goal from the start,
                i.e. in ['SPPPG'] the step count will be 4
'''
def greedy(thisGraph, mode):
    grids = thisGraph.map
    start = thisGraph.start
    goal = thisGraph.goal
    frontier = queue.PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None
    found = False

    while not frontier.empty():
        currentG = frontier.get()
        current = currentG[1]
        if current == goal:
            found = True
            break
        if mode == 0:
            for nextG in thisGraph.neighbor(current):
                if nextG not in came_from:
                    priority = manhattan(goal, nextG)
                    frontier.put((priority, nextG))
                    came_from[nextG] = current
        elif mode == 1:
            for nextG in thisGraph.diagNeighbor(current):
                if nextG not in came_from:
                    priority = chebyshev(goal, nextG)
                    frontier.put((priority, nextG))
                    came_from[nextG] = current
    if found:
        result, steps = makePath(came_from, start, goal,grids.copy())
    else:
        result = grids
        steps = 0
        
    return result, found, steps


'''
This function fill in the path on the graph with 'P',
returns the filled-in graph and the number of steps reach the goal from the start,
i.e. in ['SPPPG'] the step count will be 4
'''
def makePath(came_from, start, goal, grid):
    current = goal
    path = [current]
    
    while current != start and came_from[current] != start:
        current = came_from[current]
        curx = current[1]
        cury = current[0]
        grid[cury] = grid[cury][:curx] + 'P' + grid[cury][curx+1:]
        path.append(current)

    path.append(start)
    steps = len(path) - 1

    return grid, steps
    


def findPaths(graphList, mode):
    '''
    in a for each loop
    solve each Graph using A* and greedy at specified mode (0: manhattan, 1: chebyshev)
    returns a list of tuples containing (solution, time_spent, found_or_not, steps)
    for the aStar and Greedy both
    '''
    resultStar = []
    resultGreed = []
    
    for aGraph in graphList:
        # get the result and timestamps for aStar
        startStar = time.time()
        starSolution, foundA, stepsA = aStar(aGraph, mode)
        endStar = time.time()
        
        # get the result and timestamps for greedy
        startGreed = time.time()
        greedSolution, foundG, stepsG = greedy(aGraph, mode)
        endGreed = time.time()

        timeSpentA = endStar - startStar
        timeSpentG = endGreed - startGreed

        # put the (result, time_spent, found_or_not, steps) into the result lists
        # time_spent = end_time - start_time
        # time is in milliseconds
        resultStar.append((starSolution, timeSpentA*1000, foundA, stepsA))
        resultGreed.append((greedSolution, timeSpentG*1000, foundG, stepsG))
        
    return resultStar, resultGreed


# pretty prints a list of strings for testing purposes
def printTable(grid):
    for line in grid:
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
    g1 = graph.Graph(grids)
    frontier = queue.PriorityQueue()
    frontier.put(((2,2),3))
    frontier.put(((1,3),4))
    print(frontier.queue)
    
    print("========== GREEDY ==========")
    print()
    resultG, foundG, stepG = greedy(g1, 0)
    printTable(resultG)
    
    print()
    print("========== a* ==========")
    print()
    resultA, foundA, stepA = aStar(g1, 0)
    printTable(resultA)

##    print(g1.start)
##    print(g1.goal)
##    print(g1.neighbor([6,4]))
##    print(g1.diagNeighbor([6,4]))

    

