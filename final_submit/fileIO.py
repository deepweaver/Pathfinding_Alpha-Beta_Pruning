'''
CISC 352 - Assignment 2 - Pathfinding - pathfinding
Written by: Group 13
Date last editted: March. 11, 2019

This program has four modules, and an additional experiment module that
is only used to compile data on the performance of the two algorithms.

Main - pathfinding.py
[ fileIO.py ]
findpath.py
graph.py
experiment.py

This is the i/o module of the program.
'''

'''
This function opens the file with given name,
each line in the text file is stored as a string in a list,
the list is used to call separateGrids() function to be made into
a list of (list of strings that represents the graph)

@param name is the file name containing the graphs to be solved
@return a list of list of strings that represents the graph
'''
def readFile(name):
    inFile = open(name, 'r')
    gridLines = inFile.read().splitlines()
    grids = separateGrids(gridLines)
    inFile.close()
    return grids


'''
This function opens the file with given name,
writes the result list to the file.
with the 'w' mode each time it runs it will overwrite the content
that was already in the file.

@param result contains a list of strings of formatted output
@param outName is the name of the file to write to
'''
def writeinFile(result, outName):
    file = open(outName, 'w')
    for i in range(len(result)):
        file.write(str(result[i])+'\n')
    file.write('\n')
    file.close()


'''
This function separates the list of strings read from the file
into list of list of strings that represents the graph, the separation
is indicated by an empty line, which will be an empty list in the input list

@param gridLines contains a list of strings read from the input file
@return a list of (list of strings that represents the graph)
'''
def separateGrids(gridLines):
    grids = []
    aGrid = []
    graphX = 0
    graphY = 0
    
    for line in gridLines:
        if line != '':
            aGrid.append(line)
        else: #line == ''
            grids.append(aGrid)
            aGrid = []
            
    grids.append(aGrid)
    return grids

    
#test
if __name__ == "__main__":
    result = ["line1","line2","line3","line4"]
    writeinFile(result, "testOut.txt")
    fin = readFile('testOut.txt')
    print(fin)
