#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 01:17:24 2017
class SumBitGate that use NAND to make 1 bit sum and carry
@author: asceta
"""

from perceptron import *

class SumBitGate():
    p1 = NAND()
    p2 = NAND()
    p3 = NAND()
    p4 = NAND()
    p5 = NAND()
    
    """
    	   sumGate method recieves binary input as array. Returns binary 1 bit sum and carry
	   @param x int[2]
       @return summ, carry int
    """
    
    def sumGate(self,x1):
        
        x2=[x1[0],self.p1.act(x1)]
        x3=[self.p1.act(x1),x1[1]]
        x5=[self.p2.act(x2),self.p3.act(x3)]
        summ=self.p5.act(x5)
        
        x3=[self.p1.act(x1),self.p1.act(x1)]
        carry=self.p3.act(x3)
        
        return summ, carry
    
#small test
        
if __name__ == "__main__":
    
    gate = SumBitGate()
    summ, carry = gate.sumGate([0,0])
