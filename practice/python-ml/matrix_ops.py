import numpy as np

def transpose(M):
    rows, cols = len(M), len(M[0])
    N = build_matrix(cols,rows)
    for i in range(cols):
        for j in range(rows):
            N[i][j] = M[j][i]
    return N

def build_matrix(rows, cols):
    return [[0 for j in range(cols)] for i in range(rows)]

if __name__ == "__main__":
    A = [[1, 2, 0],[3, 5, 9]]
    print("A: ")
    print(np.matrix(A))
    B = transpose(A)
    print("B: ")
    print(np.matrix(B))
