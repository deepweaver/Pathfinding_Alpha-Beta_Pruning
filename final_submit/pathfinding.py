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

[ Main - pathfinding.py ]
fileIO.py
findpath.py
graph.py
experiment.py

This is the main module of the program.
'''

import fileIO
import graph
import findpath
import experiment
import findpath


'''
These are the globals of the program.

SIZELIST, N, and PM are defined for the experiment.
SIZELIST contains a list of sizes of graphs (for convenience purposes, all maps are squares)
N represents the number of repetition for each size
PM represent the percentage of obstacles ('X') in a row when randomly generating the graph

INFILEs are the names of the files that contains graphs to be read in.
OUTFILEs are the names of the files to write the output to.
'''
SIZELIST = [512, 1024]
N = 100
PM = 0.4
INFILE0 = "pathfinding_a.txt"
OUTFILE0 = "pathfinding_a_out.txt"
INFILE1 = "pathfinding_b.txt"
OUTFILE1 = "pathfinding_b_out.txt"


'''
This function calls the experiment function in the experiment module
using the globals defined above.
This function prints out the formatted experiment results.
'''
def doExperiment():
    star0, star1, greed0, greed1 = experiment.doExp(SIZELIST, N, PM)
    formatted = experiment.formatOutput(star0, star1, greed0, greed1, SIZELIST, N)
    experiment.printTable(formatted)
    

'''
This function calls the readFile function in the fileIO module
the list of (list of strings) that is returned is then made into
Graph object and stored in the graphList.

@param fileName is the name of the file to read the graphs from
@return a list a Graph objects
'''
def loadGraphs(fileName):
    graphs = fileIO.readFile(fileName)
    graphList = []
    for aGraph in graphs:
        graphList.append(graph.Graph(aGraph))
    return graphList


'''
This function calls the loadGraphs function to load in a list of Graphs to be solved
then calls the findPaths function in the findpath module to solve the Graphs with
the mode specified in the parameter (0 - four directions; 1 - all neighbours).
The results are then formatted and stored in a list of strings, which is used
by the writeinFile function from the fileIO module to write to file.

@param mode specifies the mode described in the program description
'''
def solveGraphs(mode):
    if mode == 0:
        outFile = OUTFILE0
        inFile = INFILE0
    elif mode == 1:
        outFile = OUTFILE1
        inFile = INFILE1
    else:
        print("Error: mode must be 0 or 1")
        return
    
    graphs = loadGraphs(inFile)
    outPath = []
    resultStar, resultGreed = findpath.findPaths(graphs, mode)

    for i in range(len(resultStar)):
        outPath.append("Greedy")
        for line in resultGreed[i][0]:
            outPath.append(line)
        outPath.append("A*")
        for line in resultStar[i][0]:
            outPath.append(line)
        outPath.append("")
    
    fileIO.writeinFile(outPath, outFile)
    return


'''
main function, calls solveGraphs at two modes
doExperiment() is commented out because it is not part of the assignment
I left the code here in case you want to play with it yourself.
'''
def main():
    solveGraphs(0)
    solveGraphs(1) 
    #doExperiment()


main()
# end of program



