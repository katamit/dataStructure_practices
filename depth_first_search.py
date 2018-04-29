#!/bin/python3

import sys
from collections import deque

def connectedCell(matrix,n,m):
    # Complete this function
    visit = []
    for j in range(n):
        a = []
        for i in range(m):
            a.append(True)
        visit.append(a)
    #print(visit)
    path = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j]:
                count = 0
                #visit[i_ind][j_ind] = 
                nodes = deque([(i,j)])
                while nodes:
                    i_ind, j_ind = nodes.pop()
                    #visit[i_ind][j_ind] = False
                    #print(i_ind,j_ind )
                    if 0 <= i_ind < n and 0 <= j_ind < m and visit[i_ind][j_ind]:
                        #print(i_ind, j_ind)
                        visit[i_ind][j_ind] = False
                        if matrix[i_ind][j_ind] == 1:
                            count += 1
                            nodes_list = [(i_ind -1, j_ind-1),
                                      (i_ind -1, j_ind),
                                      (i_ind -1, j_ind+1), 
                                      (i_ind, j_ind-1),
                                      (i_ind, j_ind+1),
                                      (i_ind +1, j_ind-1),
                                      (i_ind +1, j_ind),
                                      (i_ind +1, j_ind+1)]
                        #print(*nodes_list)
                            nodes.extend(nodes_list)
                if count > path:
                    path = count
    return path
                    
                    
                    
                

# if __name__ == "__main__":
#     n = int(input().strip())
#     m = int(input().strip())
#     matrix = []
#     for matrix_i in range(n):
#         matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
#         matrix.append(matrix_t)
#     result = connectedCell(matrix,n,m)
#     print(result)
n = 2
m = 2
matrix = [[1]*n]*m
result = connectedCell(matrix,n,m)
print('result = ',result)