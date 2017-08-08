#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 00:55:17 2017
class Test for making test over AND, OR, NAND & summing bit gates
@author: asceta
"""

from perceptron import *
from sum import *

class Test:
    p_AND = AND()
    p_OR = OR()
    p_NAND = NAND()
    gate = SumBitGate()
    
    def testAND(self):
        assert self.p_AND.act([0,0])==0
        assert self.p_AND.act([0,1])==0
        assert self.p_AND.act([1,0])==0
        assert self.p_AND.act([1,1])==1
        
    def testOR(self):
        assert self.p_OR.act([0,0])==0
        assert self.p_OR.act([0,1])==1
        assert self.p_OR.act([1,0])==1
        assert self.p_OR.act([1,1])==1
        
    def testNAND(self):
        assert self.p_NAND.act([0,0])==1
        assert self.p_NAND.act([0,1])==1
        assert self.p_NAND.act([1,0])==1
        assert self.p_NAND.act([1,1])==0
        
    def testSumBitGate(self):
        summ, carry = self.gate.sumGate([0,0])
        assert [summ, carry]==[0,0]
        summ, carry = self.gate.sumGate([0,1])
        assert [summ, carry]==[1,0]
        summ, carry = self.gate.sumGate([1,0])
        assert [summ, carry]==[1,0]
        summ, carry = self.gate.sumGate([1,1])
        assert [summ, carry]==[0,1]
        
if __name__ == "__main__":
    T=Test()
    T.testAND()
    T.testOR()
    T.testNAND()
    T.testSumBitGate()