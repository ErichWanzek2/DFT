"""discrete fuorier transform"""
import numpy as np
import matplotlib.pyplot as plt
N=5
a=5
###################################################################
def xmesh(a,N):
    """This function generates the a mesh of x values
    INPUTS: N(number of steps),interval (tuple (a,b))
    OUTPUTS: xmesh1, xmesh2
    """
    h = (2*a)/N
    xmesh=np.zeros((1,N))
    for i in range(N-1):
        xmesh[0,i]=(-a+i*h)
    xmesh[0,0]=-a
    xmesh[0,N-1]=a
    return xmesh
###################################################################   
def function(x):
    return np.sin(x)
###################################################################
def functionlist(xmesh,N):
    H=np.zeros((1,N))
    for i in range(N-1):
        H[0,i]=function(xmesh[0,i])
    return H
###################################################################
def generate_DFT_function(functionlist,N,n):
    DFTtermlist=np.zeros((1,N))
    for i in range(N-1):
        DFTtermlist[0,i]=(functionlist[0,i])*np.exp((2*(np.pi)*n)/N)
    return np.sum(DFTtermlist)
###################################################################        
def n_mesh(a,N):
    """This function generates the a mesh of x values
    INPUTS: N(number of steps),interval (tuple (a,b))
    OUTPUTS: xmesh1, xmesh2
    """
    h = (2*a)/N
    nmesh=np.zeros((1,N))
    for i in range(N-1):
        nmesh[0,i]=(-a+i*h)
    nmesh[0,0]=-a
    nmesh[0,N-1]=a
    return nmesh
#####################################################################
def DFTfunction(n):
    return generate_DFT_function(functionlist(xmesh(a,N),N),N,n)
#####################################################################
def DFTlist(xmesh,nmesh,N):
    DFT=np.zeros((1,N))
    for i in range(N-1):
        DFT[0,i]=DFTfunction(xmesh[0,i])
    return DFT
#####################################################################
def plot_functions(xmesh,nmesh,N,functionlist,DFTlist): 
    plt.plot(xmesh,functionlist)
    plt.plot(nmesh,DFTlist)
    plt.show
#####################################################################
def run():
    xmesh1=xmesh(a,N)
    functionlist1=functionlist(xmesh1,N)
    nmesh1=n_mesh(a,N)
    DFTlist1=DFTlist(xmesh1,nmesh1,N)
    plot_functions(xmesh1,nmesh1,N,functionlist1,DFTlist1)
    return

run()

    
    
    
    
    














