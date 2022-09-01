import numpy

# This function performs a sanity check before matrix operations
def sanityCheck(matrix):

    rowNum = len(matrix)
    colNum = len(matrix[0]) if rowNum > 0 else 0

    if(rowNum == 0 or rowNum == 0):
        return False

    for row in matrix:
        if len(row) != colNum:
            return False

    return True;

def docMatch(preferenceMatrix):
    sanityCheck()
    return

docMatch()