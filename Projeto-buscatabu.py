#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 01:14:49 2018

@author: laura
"""

import numpy as np

def func(n,sbarra):
    s=0   
    for i in range(n):
        if sbarra[i]==1:
            s=2**i+s
            
    s=(1/(2**(n)-1))*s
    if(s<=1) and (s>=0):
        s=100*np.sin(10*s)*np.cos(7*s)
    return s
    

def aspiracao(n,T,sbarra):

    s=0
    k=0
    tbarra=np.zeros(n)
    temp=0
    
    for i in range(n):
        for j in range(n):
            if T[i,j]==1:
                temp=temp+2**j
        temp=(1/(2**(n)-1))*temp
        if(temp<=1) and (temp>=0):
            temp=100*np.sin(10*temp)*np.cos(7*temp)
        
        tbarra[i]=temp
        temp=0
    
    for i in range(n):
        if sbarra[i]==1:
            s=2**i+s
    s=(1/(2**(n)-1))*s
    if(s<=1) and (s>=0):
        s=100*np.sin(10*s)*np.cos(7*s)
    
    for i in range(n):
        if s>tbarra[i]:
            k=1
    return k
    

n=20
sbarra=[0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0]
sestrela=np.zeros(n)
s0=np.zeros(n)
itera=0
melhoritera=0
btmax=n
cont=0
T=np.zeros((n,n))
l=0
maior=0
tabu=0
s=np.zeros(n)
temp1=np.zeros(n)
temp2=np.zeros(n)
while((itera - melhoritera)<=btmax):
    itera=itera+1
    for i in range(n): #fazendo o movimento m
        cont=0
        if sbarra[i]==1:
            sbarra[i]=0
        else:
            sbarra[i]=1
            
        for j in range(n):
            if sbarra[j]==1:
                s[i]=2**i+s[i]
            if s[i]>=maior:
                maior=s[i]
        for j in range(n):
            for k in range(n):
                if(T[j,k]==sbarra[k]):
                    cont=cont+1
        if cont==n:
            tabu=i
        if sbarra[i]==1:
            sbarra[i]=0
        else:
            sbarra[i]=1
    print(maior)
          
        

    for i in range(n):
        if(s[i]==maior):
            if sbarra[i]==0:
                sbarra[i]=1
            else:
                sbarra[i]=0
    #print(s[:])
    maior=0
    for j in range(n):
        cont=0
        for k in range(n):
            if(T[j,k]==sbarra[k]):
                cont=cont+1
    l=aspiracao(n,T,sbarra)
    if cont==n: #conferindo se eh tabu
        if l==1: #verificando funcao de asp
            temp1=T[0,:]
            temp2=temp1
            T[0,:]=sbarra
            for i in range(n-1): #ATUALIZANDO A LISTA TABU
                temp2=T[i+1,:]
                T[i+1,:]=temp1
                temp1= temp2
    else:
        temp1=T[0,:]
        temp2=temp1
        T[0,:]=sbarra
        for i in range(n-1): #ATUALIZANDO A LISTA TABU
            temp2=T[i+1,:]
            T[i+1,:]=temp1
            temp1= temp2
            print (T[:,:])
    if (func(n,sbarra)>func(n,sestrela)):
        sestrela[:]=sbarra[:]
        melhoritera=itera
    temp1=np.zeros(n)
    temp2=np.zeros(n)
        
s=0
for i in range(n):
    if sestrela[i]==1:
        s=2**i+s
s=(1/(2**n-1))*s

print (s)
print (melhoritera)
print (func(n,sestrela))
print (T[:,:])