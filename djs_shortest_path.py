#!/usr/bin/env python
# coding=utf-8
import numpy as np

_=float('inf')
N=5

def shortest_path(graph,n):
    dis=[0]*N
    flag=[False]*N
    min_index=0
    flag[n]=True
    mini=0

    for i in range(N):
        dis[i] = graph[n][i]

    f=lambda x:[True for i in range(N)]
    while f(1)!=flag:
        mini=_
        for i in range(N):
            if dis[i]<=mini and not flag[i]:
                mini = dis[i]
                min_index=i
        if min_index==n:
            return       #unconnect

        flag[min_index]=True
        for j in range(N):
            if dis[j]>dis[min_index]+graph[min_index][j]:
                dis[j]=dis[min_index]+graph[min_index][j]

    print("the shortest path is:{0}".format(dis))


def main():
    graph=[[0,100,30,_,10],\
         [_,0,_,_,_],\
         [_,60,0,60,_],
         [_,10,_,0,_],
         [_,_,_,50,0]]
    print("please input n:")
    n=int(input())
    shortest_path(graph,n)

if __name__ == "__main__":
    main()
