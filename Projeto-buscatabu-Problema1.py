#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 20:55:29 2018

@author: laura
"""


############## Inicio do algoritmo

import numpy as np

########funcao a ser maximizada

def funcao(x):
    f=0.0
    if (x<=1.0) and (x>=0.0):
        f=100*np.sin(10*x)*np.cos(7*x)
    return f


######funcao de aspiracao 

def aspiracao(n,solucaolinha,solucaoatual):
    naoehmaistabu=0
    
    sl=0.0

    for i in range(n):
        if solucaolinha[i]==1:
            sl=sl+2**i
    sl=(sl/(2**n-1))
    sa=0.0

    for i in range(n):
        if solucaoatual[i]==1:
            sa=sa+2**i
    sa=(s/(2**n-1))
    fsolucaolinha=funcao(sl)
    fsolucaoatual=funcao(sa)
    if(fsolucaolinha>fsolucaoatual):
        naoehmaistabu=1
    return naoehmaistabu

############movimento da vizinhanca

def movimento(n,Tabu,solucaoatual):
    melhormovimento=solucaoatual
    contador=0
    xbarra=0.0
    maior=0.0
    for i in range(n):
        if(melhormovimento[i]==1):
            melhormovimento[i]=0
        else:
            melhormovimento[i]=1
        for k in range(n):
            if melhormovimento[k]==1:
                xbarra=xbarra+2**k
        xbarra=(xbarra/(2**n-1))
        if(funcao(xbarra)>=maior):
            maior=funcao(xbarra)
        if(melhormovimento[i]==1):
            melhormovimento[i]=0
        else:
            melhormovimento[i]=1
    xbarra=0.0
        
    for i in range(n):
        if(melhormovimento[i]==1):
            melhormovimento[i]=0
        else:
            melhormovimento[i]=1
        for k in range(n):
            if melhormovimento[k]==1:
                xbarra=xbarra+2**k
        xbarra=(xbarra/(2**n-1))

        if(maior==funcao(xbarra)):        
            for k in range(n):
                contador=0
                for j in range(n):
                    if(Tabu[k,j]==melhormovimento[j]):
                        contador=contador+1
                if(contador>(n-1)):
                    if(aspiracao(n,melhormovimento,solucaoatual)==1):
                        return melhormovimento
                       
                else:
                    return melhormovimento         
        if(melhormovimento[i]==1):
            melhormovimento[i]=0
        else:
            melhormovimento[i]=1

    
    
    

######atualizar lista tabu

def atualizarlista(n,Tabu,solucaoatual):
    temp1=Tabu[0,:]
    temp2=temp1
    Tabu[0,:]=solucaoatual
    for i in range(1,n):
        temp2=Tabu[i,:]
        Tabu[i,:]=temp1
        temp1=temp2
        




###### parametros
n=10
solucaoatual=[1,0,1,1,0,0,0,0,0,0]
solucaootima=solucaoatual
iteracaoatual=0
solucaolinha=np.zeros(n)
melhoriteracao=0
btmax=10
Tabu=np.zeros((n,n))

######algoritmo

while((iteracaoatual-melhoriteracao)<=btmax):
    iteracaoatual=iteracaoatual+1
    solucaoatual=movimento(n,Tabu,solucaoatual)
    atualizarlista(n,Tabu,solucaoatual)
    sa=0.0

    for i in range(n):
        if solucaoatual[i]==1:
            sa=sa+2**i
    sa=(sa/(2**n-1))
    
    so=0.0

    for i in range(n):
        if solucaootima[i]==1:
            so=so+2**i
    so=(so/(2**n-1))
    if(funcao(sa)>funcao(so)):
        solucaootima=solucaoatual
        melhoriteracao=iteracaoatual
s=0.0

for i in range(n):
    if solucaoatual[i]==1:
        s=s+2**i
s=(s/(2**n-1))

print(solucaootima)
print(s)
print(funcao(s))