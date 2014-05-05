from numpy import *
from sys import argv
from distancetree import *

readCSV = lambda path: [l.split(",") for l in file(path).read().splitlines()]
head    = lambda arr: arr[0]
tail    = lambda arr: arr[1:]
rptsum  = lambda arr: repeat(sum(arr), size(arr))
map2    = lambda fn, mat: map(lambda arr: map(fn, arr), mat)
mapvsum = lambda mat: matrix(map(rptsum, mat))
maphsum = lambda mat: mapvsum(mat).transpose()
idxmin  = lambda mat: unravel_index(argmin(mat), shape(mat))
exists  = lambda x: x != None
wraparr = lambda x: [x]

# Remove rows and columns of matrix with the listed indices
withoutIndices = lambda m, ids: delete(delete(m, ids, axis=0), ids, axis=1)
# Append a vector as both a row and a column
appendRowCol   = lambda m, v: hstack((vstack((m, [v])), map(wraparr, v + [0])))

def neighborJoin(D, forest):
    if len(D) == 2:
        return Tree(forest[0], forest[1])
    SH = mapvsum(D)
    SV = SH.transpose()
    I = identity(len(D))
    M = D + (multiply(I, SH + SV) - SH - SV) / (len(D) - 2)
    i, j = idxmin(M)
    u = [(D[i,k] + D[j,k] - D[i,j]) / 2 for k in range(len(D))]
    #su  = (D[i,j] + SH[i,j] - SV[i,j]) / 2
    dui = (D[i,j] + SH[i,j] - SV[i,j]) / 2
    duj = (D[j,i] + SH[j,i] - SV[j,i]) / 2
    forest = hstack((forest, [Tree(forest[i], forest[j], dui, duj)]))
    D = appendRowCol(D, u)
    D = withoutIndices(D, (i, j))
    forest = delete(forest, (i, j))
    return neighborJoin(D, forest)

if __name__ == "__main__":
    cells = readCSV(argv[1])
    forest = array(map(Leaf, tail(head(cells))))
    D = matrix(map2(float, tail(map(tail, cells))))
    tree = neighborJoin(D, forest)
    print tree
