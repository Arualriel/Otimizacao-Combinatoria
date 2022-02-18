#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 22:27:13 2018

@author: laura
"""

#############Inicio do algoritmo

import numpy as np

########funcao a ser maximizada

def funcao(x,y,z):

    f=0
    if (x+y+z<=1000) and (x>=0) and (y>=0) and (z>=0):
        f=x*y*z+7*x*y+4*y*z-5*x*z-y**3-95*z**2
    return f


######funcao de aspiracao
    
def aspiracao(n,solucaolinhax,solucaolinhay,solucaolinhaz,solucaoatualx,solucaoatualy,solucaoatualz):
    naoehmaistabu=0
    slx=0.
    sly=0.
    slz=0.
    for i in range(n):
        if solucaolinhax[i]==1:
            slx=slx+2**i
    slx=((slx*10000)//(2**n-1))
    for i in range(n):
        if solucaolinhay[i]==1:
            sly=sly+2**i
    sly=((sly*10000)//(2**n-1))
    for i in range(n):
        if solucaolinhaz[i]==1:
            slz=slz+2**i
    slz=((slz*10000)//(2**n-1))
    
    sax=0.
    say=0.
    saz=0.
    for i in range(n):
        if solucaoatualx[i]==1:
            sax=sax+2**i
    sax=((sax*10000)//(2**n-1))
    for i in range(n):
        if solucaoatualy[i]==1:
            say=say+2**i
    say=((say*10000)//(2**n-1))
    for i in range(n):
        if solucaoatualz[i]==1:
            saz=saz+2**i
    saz=((saz*10000)//(2**n-1))


    fsolucaolinha=funcao(slx,sly,slz)

    fsolucaoatual=funcao(sax,say,saz)

    if(fsolucaolinha>fsolucaoatual):
        naoehmaistabu=1
    return naoehmaistabu

############movimento da vizinhanca

def movimento(n,Tabux,Tabuy,Tabuz,solucaoatualx,solucaoatualy,solucaoatualz):
    melhormovimentox=solucaoatualx
    melhormovimentoy=solucaoatualy
    melhormovimentoz=solucaoatualz
    contadorx=0
    contadory=0
    contadorz=0
    xbarra=0.0
    ybarra=0.0
    zbarra=0.0
    maiorx=0
    maiory=0
    maiorz=0
    for i in range(n):
        xbarra=0.0
        ybarra=0.0
        zbarra=0.0
        
        if(melhormovimentox[i]==1):
            melhormovimentox[i]=0
        else:
            melhormovimentox[i]=1
        for k in range(n):
            if melhormovimentox[k]==1:
                xbarra=xbarra+2**k
        xbarra=((xbarra*10000)//(2**n-1))
        
        if(funcao(xbarra,0,0)>=maiorx):
            
            maiorx=funcao(xbarra,0,0)
        

        if(melhormovimentoy[i]==1):
            melhormovimentoy[i]=0
        else:
            melhormovimentoy[i]=1
        for k in range(n):
            if melhormovimentoy[k]==1:
                
                ybarra=ybarra+2**k
        
        ybarra=((ybarra*10000)//(2**n-1))
        
        if(funcao(0,ybarra,0)>=maiory):
            
            maiory=funcao(0,ybarra,0)
    

        if(melhormovimentoz[i]==1):
            melhormovimentoz[i]=0
        else:
            melhormovimentoz[i]=1
        for k in range(n):
            if melhormovimentoz[k]==1:
                zbarra=zbarra+2**k
        
        zbarra=((zbarra*10000)//(2**n-1))
        if(funcao(0,0,zbarra)>=maiorz):
            
            maiorz=funcao(0,0,zbarra)

    for i in range(n):
        if(melhormovimentox[i]==1):
            melhormovimentox[i]=0
        else:
            melhormovimentox[i]=1


    for i in range(n):
        if(melhormovimentoy[i]==1):
            melhormovimentoy[i]=0
        else:
            melhormovimentoy[i]=1


    for i in range(n):
        if(melhormovimentoz[i]==1):
            melhormovimentoz[i]=0
        else:
            melhormovimentoz[i]=1
    
    xbarra=0.0
    ybarra=0.0
    zbarra=0.0




        
    for i in range(n):
        if(melhormovimentox[i]==1):
            melhormovimentox[i]=0
        else:
            melhormovimentox[i]=1

        if(melhormovimentoy[i]==1):
            melhormovimentoy[i]=0
        else:
            melhormovimentoy[i]=1

        if(melhormovimentoz[i]==1):
            melhormovimentoz[i]=0
        else:
            melhormovimentoz[i]=1


        for k in range(n):
            if melhormovimentox[k]==1:
                xbarra=xbarra+2**k
            if melhormovimentoy[k]==1:
                ybarra=ybarra+2**k                
            if melhormovimentoz[k]==1:
                zbarra=zbarra+2**k
        xbarra=((xbarra*10000)//(2**n-1))  
        ybarra=((ybarra*10000)//(2**n-1))
        zbarra=((zbarra*10000)//(2**n-1))
      
        if(maiorx<=funcao(xbarra,ybarra,zbarra)) and (maiory<=funcao(xbarra,ybarra,zbarra)) and (maiorz<=funcao(xbarra,ybarra,zbarra)):        
            
            for k in range(n):
                contadorx=0
                contadory=0
                contadorz=0
                for j in range(n):
                    if(Tabux[k,j]==melhormovimentox[j]):
                        
                        contadorx=contadorx+1

                for j in range(n):
                    if(Tabuy[k,j]==melhormovimentoy[j]):
                        contadory=contadory+1

                for j in range(n):
                    if(Tabuz[k,j]==melhormovimentoz[j]):
                        contadorz=contadorz+1

                if(contadorx==n) or (contadory==n) or (contadorz==n):
                    if(aspiracao(n,melhormovimentox,melhormovimentoy,melhormovimentoz,solucaoatualx,solucaoatualy,solucaoatualz)==1):
                        
                        solucaoatualx=melhormovimentox
                        solucaoatualy=melhormovimentoy
                        solucaoatualz=melhormovimentoz
                        return solucaoatualx,solucaoatualy,solucaoatualz
                else:
                    solucaoatualx=melhormovimentox
                    solucaoatualy=melhormovimentoy
                    solucaoatualz=melhormovimentoz
                    return solucaoatualx,solucaoatualy,solucaoatualz
    

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

n=9


solucaoatualx=[1,1,0,1,1,0,0,0,0]
solucaoatualy=[0,1,1,0,0,0,0,0,0]
solucaoatualz=[0,0,1,1,0,0,0,0,0]
solucaootimax=solucaoatualx
solucaootimay=solucaoatualy
solucaootimaz=solucaoatualz

iteracaoatual=0
solucaolinha=np.zeros(n)
melhoriteracao=0
btmax=11
Tabux=np.zeros((n,n))
Tabuy=np.zeros((n,n))
Tabuz=np.zeros((n,n))

###### algoritmo

while((iteracaoatual-melhoriteracao)<=btmax):
    iteracaoatual=iteracaoatual+1
    solucaoatualx,solucaoatualy,solucaoatualz=movimento(n,Tabux,Tabuy,Tabuz,solucaoatualx,solucaoatualy,solucaoatualz)
    atualizarlista(n,Tabux,solucaoatualx)
    atualizarlista(n,Tabuy,solucaoatualy)
    atualizarlista(n,Tabuz,solucaoatualz)
    
    sox=0.
    soy=0.
    soz=0.
    for i in range(n):
        if solucaootimax[i]==1:
            sox=sox+2**i
    sox=((sox*10000)//(2**n-1))
    for i in range(n):
        if solucaootimay[i]==1:
            soy=soy+2**i
    soy=((soy*10000)//(2**n-1))
    for i in range(n):
        if solucaootimaz[i]==1:
            soz=soz+2**i
    soz=((soz*10000)//(2**n-1))

    
    sax=0.
    say=0.
    saz=0.
    for i in range(n):
        if solucaoatualx[i]==1:
            sax=sax+2**i
    sax=((sax*10000)//(2**n-1))
    for i in range(n):
        if solucaoatualy[i]==1:
            say=say+2**i
    say=((say*10000)//(2**n-1))
    for i in range(n):
        if solucaoatualz[i]==1:
            saz=saz+2**i
    saz=((saz*10000)//(2**n-1))

    
    
    if(funcao(sax,say,saz)>funcao(sox,soy,soz)):
        solucaootimax=solucaoatualx
        solucaootimay=solucaoatualy
        solucaootimaz=solucaoatualz
        melhoriteracao=iteracaoatual
    
sx=0.
sy=0.
sz=0.
for i in range(n):
    if solucaootimax[i]==1:
        sx=sx+2**i
sx=((sx*10000)//(2**n-1))
for i in range(n):
    if solucaootimay[i]==1:
        sy=sy+2**i
sy=((sy*10000)//(2**n-1))
for i in range(n):
    if solucaootimaz[i]==1:
        sz=sz+2**i
sz=((sz*10000)//(2**n-1))


print(solucaootimax)
print(solucaootimay)
print(solucaootimaz)

print(sx)
print(sy)
print(sz)
print(funcao(sx,sy,sz))