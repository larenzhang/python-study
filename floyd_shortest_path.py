#!/usr/bin/env python
# coding=utf-8
import numpy as np

_=float('inf')
N=5

def get_shortest_path(graph):
    path=np.full((N,N),-1,int)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j]>graph[i][k]+graph[k][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]
                    path[i][j]=k

    print("graph is:{0}".format(graph))
    print("path:{0}".format(path))

def main():
    graph=[[0,100,30,_,10],\
           [_,0,_,_,_],\
           [_,60,0,60,_],
           [_,10,_,0,_],
           [_,_,_,50,0]]

    get_shortest_path(graph)

if __name__ == "__main__":
    main()
