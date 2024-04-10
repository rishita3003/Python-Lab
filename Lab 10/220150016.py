# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:03:43 2024

Rishita Agarwal
220150016
Graded lab 10

@author: hp
"""

#task 1
list1=[6,6,12,18,30]
list2=[5,6,11,18,29]

len1=len(list1)
len2=len(list2)

flag=0

for i in range(0,len1-2):
    if(list1[i]+list1[i+1]!=list1[i+2]):
        flag=1
        break

if(flag):
    print("List 1 is not an additive sequence.")
else:
    print("List 1 is an additive sequence.")
    
flag=0

for i in range(0,len2-2):
    if(list2[i]+list2[i+1]!=list2[i+2]):
        flag=1
        break;

if(flag):
    print("List 2 is not an additive sequence.")
else:
    print("List 2 is an additive sequence.")



#task 2
  
import math

c=[[1.0,1.0,15.0],[2.0,2.0,35.0]]

x=[[1.4,0.6,20.0],[0.2,0.5,55.0],[0.0,1.1,56.0],[0.7,1.6,58.0],[2.3,3.1,49.0],[0.3,4.7,23.0]]
data_len=len(x)

#euclidean distance
def eucl_dis(a,b,dimensions):
    sum=0
    for dim in range(0,dimensions):
        sum+=(a[dim]-b[dim])*(a[dim]-b[dim])
        
    return math.sqrt(sum)
        
iterations=4
k=len(c) #number of clusters
dimensions=len(c[0])

d=[[0 for _ in range(data_len)] for _ in range(k)]

clusters=[[] for _ in range(k)] #new clusters assignment

for it in range(0,iterations):
    for point in range(0,data_len):
        minm=float('inf')
        cluster=0 #initialized as 0
        for cl in range(0,k):
            d[cl][point]=eucl_dis(x[point],c[cl],dimensions)
            #assigning the point to the cluster to which it is closest
            if(d[cl][point]<minm):
                minm=d[cl][point]
                cluster=cl
        #appending the points to their respective clusters
        clusters[cluster].append(x[point])

    #finding new centers by taking the mean of the points in the cluster
    for cl in range(0,k):
        sum=[0 for _ in range(dimensions)]
        for point in clusters[cl]:
            for dim in range(0,dimensions):
                sum[dim]+=point[dim]
        if clusters[cl]:  # Check if cluster is not empty to avoid division by zero as undefined
            c[cl]=[sum[dim]/len(clusters[cl]) for dim in range(0,dimensions)]
            
    print("Iteration", it + 1)
    print(f"clusters {it+1}: ",clusters)
    clusters=[[] for _ in range(k)]  # Clear clusters for next iteration storage
    print(f"centers {it+1}: ",c)

    
#task 3

import numpy as np
import math

#x as the data points, c as the centers and m sas the number of dimenstions
#p is not specially assigned so p=m here

#updating the initialization matrix
def update_u(x, c, m):
    n = len(x) #number of data points
    k = len(c) #number of clusters
    u = np.zeros((k, n)) 
    for i in range(n):
        for j in range(k):
            sum = 0
            for l in range(k):
                sum += (np.linalg.norm(x[i] - c[j]) / np.linalg.norm(x[i] - c[l])) ** (2 / (m - 1))
            u[j][i] = 1 / sum
    return u

#updating the centers
def update_c(x, u, m):
    n = len(x)
    k = u.shape[0]
    c = np.zeros((k, x.shape[1]))
    for j in range(k):
        sum1 = 0
        sum2 = 0
        for i in range(n):
            sum1 += (u[j][i] ** m) * x[i]
            sum2 += u[j][i] ** m
        c[j] = sum1 / sum2
    return c

#fuzzy c means algorithm
def fcm(x, c, m, max_iter):
    n=len(x)
    k=len(c)
    for i in range(max_iter):
        #assigning clusters before every iteration
        clusters=[[] for _ in range(k)]
        #forming the distance matrix of everypoint from every cluster using euclidean distance
        for j in range(n):
            for l in range(k):
                d[l][j]=eucl_dis(c[l],x[j],m)
                
        #traversing in the distance matrix to assign points to differnt clusters
        for j in range(n):
            minm=d[0][j] #minm assigned as distance from the 1st cluster
            cluster=0
            for l in range(k):
                if d[l][j]<minm:
                    minm=d[l][j]
                    cluster=l
            #assigning the data point to the cluster to which it is closest
            clusters[cluster].append(x[j])
        
        #once the points are assigned to the clusters
        
        #update the u matrix using the formula and function defined above
        u = update_u(x, c, m)
        
        #after updating the u matrix, now new centers would be updated
        c = update_c(x, u, m)
        
        #again the perform the iterations using the updated values
        #print(f"u{i+1}: ",u)
        #print(f"c{i+1}: ",c)
        print(f"clusters {i+1}: ",clusters)
    return u, c  

x = np.array([[1, 3], [1.5, 3.2], [1.3, 2.8], [3, 1]])
u=np.array([[0.7,0.9,0.3,0.9], [0.3,0.1,0.7,0.1]])
m=x.shape[1]
c=update_c(x,u,m)
max_iter = 10
u, c = fcm(x, c, m, max_iter)
print(u)
print(c)




