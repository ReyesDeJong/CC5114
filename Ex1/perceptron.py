#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 23:19:22 2017
class Perceptron as AND, OR & NAND gates
@author: Esteban Reyes de Jong
"""

class Perceptron:
    'Common base class for all perceptrons'
    '''
        contructor input: two weights and bias
	   @param weight1 doble (first weight)
	   @param weight2 double (second weight)
	   @param bias double (bias)
    '''
    def __init__(self, w1, w2, b):
        self.weight1 = w1 
        self.weight2 = w2 
        self.bias = b
      
    """
	   Output method recieves binary input as array. Returns 1 or 0 if condition met
	   @param x int[2]
       @return act int
    """
   
    def act(self, x):
       
       f=(x[0]*self.weight1 + x[1]*self.weight2 + self.bias)
       if(f<=0):
           return 0
       else:
           return 1
"""
Classes AND, OR, NAND, inherited from perceptron class
Used to inicialice weight according to distinct gates
"""
      
class AND(Perceptron):
    
    def __init__(self):
        super().__init__(0.5, 0.5, -0.5)
        
class OR(Perceptron):
    
    def __init__(self):
        super().__init__(0.5, 0.5, 0)

class NAND(Perceptron):
    
    def __init__(self):
        super().__init__(-0.5, -0.5, 0.75)      

#small tests
if __name__ == "__main__":
#    main()
    p_AND = AND()
    out_AND = p_AND.act([1,1])
    p_OR = OR()
    out_OR = p_OR.act([0,0])
    p_NAND = NAND()
    out_NAND = p_NAND.act([0,0])