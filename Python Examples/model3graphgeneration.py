#!/usr/bin/env python
"""
Read and write graphs.
"""
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
#    Copyright (C) 2004-2006 by 
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.import pylab
import matplotlib.pyplot as plt
import networkx as nx
from networkx import *
import pylab
import math

U=nx.random_geometric_graph(100,10)
pos=nx.get_node_attributes(U,'pos')
q= open("model3.txt", "w" )
T=str(pos)
print pos
q.write(T)
for node in U:
    pylab.clf()
    if pos is not None:
        for n in pos:
            pos=nx.random_layout(U)
            plt.figure()
            nx.draw_networkx_nodes(U,pos)
            plt.xlim(-0.1,1.1)
            plt.ylim(-0.1,1.1)
            pylab.title("MODEL 3")
            pylab.draw()
            pylab.savefig("model3.png")
                
q.close()

