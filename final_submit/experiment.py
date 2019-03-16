import graph
import random
import findpath

'''
CISC 352 - Assignment 2 - Pathfinding - pathfinding
Written by: Group 13
Date last editted: March. 11, 2019

This program has four modules, and an additional experiment module that
is only used to compile data on the performance of the two algorithms.

Main - pathfinding.py
fileIO.py
findpath.py
graph.py
[ experiment.py ]

This is the experiment module
This module does performance analysis on the A* and Greedy algorithms
by generating N graphs for a list of graph sizes. For convenience
purposes, all graphs are squares (m*m).
'''


def doExp(sizeList, n, pm):
    '''
    Procedure:
    1) randomly generate N graphs for each size in the sizeList, store in graphList
    2) for each graph in the graphList, find path using A* and Greedy,
       at mode 0 and 1. (0: only 4 directions; 1: in all directions)
    3) The results are stored in 4 lists:
           - star0: result from using aStar at mode 0
           - star1: result from using aStar at mode 1
           - greed0: result from using greedy at mode 0
           - greed1: result from using greedy at mode 1
    4) The results are stored as tuples: (solution, time_spent, found_or_not, steps)

    returns 4 result lists for A* and Greedy at the two different modes
    '''
    graphList = generateGraphs(sizeList, n, pm)

    star0, greed0 = findpath.findPaths(graphList, 0)
    star1, greed1 = findpath.findPaths(graphList, 1)

    return star0, star1, greed0, greed1


def makeGrid(m, n, pm):
    '''
    randomly generate a graph
    '''
    aTable = (['X' * (int(m*pm)) + '_' * (m - int(m*pm))]) * n
    grid = []
    for i in range(n):
        listStr = list(aTable[i])
        random.shuffle(listStr)
        grid.append(''.join(listStr))
    startx = random.randint(0, m-1)
    starty = random.randint(0, n-1)
    endx = random.randint(0, m-1)
    endy = random.randint(0, n-1)

    while startx == endx and starty == endy:
        endx = random.randint(0, m-1)
        endy = random.randint(0, n-1)

    grid[starty] = grid[starty][:startx] + 'S' + grid[starty][startx+1:]
    grid[endy] = grid[endy][:endx] + 'G' + grid[endy][endx+1:]

    return grid


def generateGraphs(sizeList, n, pm):
    '''
    for each value in the sizeList, generate n graphs of that size
    returns a list of graphs objects
    this function is used to compile data
    on the performance of the two algorithms
    '''
    graphList = []
    for s in sizeList:
        for i in range(n):
            strGraph = makeGrid(s,s,pm)
            gGraph = graph.Graph(strGraph)
            graphList.append(gGraph)

    return graphList


def formatOutput(star0, star1, greed0, greed1, sizeList, n):
    '''
    result: (solution, timeSpent, found_or_not, step)

    The results for the experiment is output to a txt file
    will be formatted as below

    size = s1
    method    mode    time(avg)    steps(avg)    numSuccess
    aStar     0
    greedy    0
    aStar     1
    greedy    1

    size = s2
    .
    .
    .
    
    returns a list of strings to be written to file
    '''
    formatted = []
    index = 0
    for s in range(len(sizeList)):
        line = "size = " + str(sizeList[s])
        formatted.append(line)
        formatted.append("method\tmode\ttime(avg)\tsteps(avg)\tnumSuccess")
        timeList = []
        stepList = []
        line1 = "aStar\t0\t" + formatALine(star0, n, index)
        line2 = "greedy\t0\t" + formatALine(greed0, n, index)
        line3 = "aStar\t1\t" + formatALine(star1, n, index)
        line4 = "greedy\t1\t" + formatALine(greed1, n, index)
        index += n

        formatted.append(line1)
        formatted.append(line2)
        formatted.append(line3)
        formatted.append(line4)
    return formatted


def formatALine(rList, n, index):
    '''
    gets a list of results, result: (solution, timeSpent, found_or_not, step)
    calculates the average timeSpent and step for the cases where a path can be found
    format it into:
    [avgTime]    [avgStep]    [numSuccess]
    in which a '\t' separates each data item,
    and the averages keeps 5 digits after decimal point
    '''
    retString = ""
    numSuccess = 0
    time = []
    step = []
    for i in range(n):
        if rList[i+index][2]:
            time.append(rList[i+index][1])
            step.append(rList[i+index][3])
            numSuccess += 1
    avgTime = sum(time)/len(time)
    avgStep = sum(step)/len(step)
    timeStr = "{:8.5f}".format(avgTime)
    stepStr = "{:8.5f}".format(avgStep)
    retString += timeStr + "\t" + stepStr + "\t" + str(numSuccess)
    return retString
    
    
    

# for testing purpose only, delet before submition
def printTable(grid):
    for line in grid:
        print(line)

def printResults(resultList):
    for result in resultList:
        resultGraph = result[0]
        time = result[1]
        found = result[2]
        step = result[3]
        size = len(resultGraph)
        print()
        print("printing result for size =", size)
        
        if not found:
            print("can not find the path")
        '''
        else:
            printTable(resultGraph)
        '''
        print("time spend =", time, "millisec")
        print("path length is", step, "steps")
        print()
        
        


if __name__ == "__main__":
    sizeList = [16, 32]
    n = 5
    pm = 0.4
    
    # Test for generateGraphs function
    graphList = generateGraphs(sizeList, n, pm)
    for g in graphList:
        printTable(g.map)
        print()
    
    
    star0, star1, greed0, greed1 = doExp(sizeList, n, pm)
    
    print("\nFor aStar mode 0 ======================\n")
    printResults(star0)
    print("\nFor aStar mode 1 ======================\n")
    printResults(star1)
    print("\nFor greedy mode 0 ======================\n")
    printResults(greed0)
    print("\nFor greedy mode 1 ======================\n")
    printResults(greed1)
    
    formatted = formatOutput(star0, star1, greed0, greed1, sizeList, n)
    printTable(formatted)
    
