#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wen Aug  9 23:19:22 2017
class Perceptron and its trainning
@author: asceta
"""
import random
import matplotlib.pyplot as plt
import operator
import math as m

class Perceptron:
    'Common base class for all perceptrons'
    '''
        contructor input: two weights and bias
	   @param weight1 doble (first weight)
	   @param w2 double (second weight)
	   @param d double (bias)
       @param w double (bias and weight list)
       @param acc (list of trainning accuracies)
    '''
    def __init__(self, w1=random.randint(0,100)/100, w2=random.randint(0,100)/100 , b=random.randint(0,100)/100):
        self.weight1 = w1 
        self.weight2 = w2 
        self.bias = b
        self.w = [self.bias, self.weight1, self.weight2]
        self.acc=[]

     
        
    """
	   act method recieves binary input as array. Returns sigmoide activation (1 or 0 if condition met)
	   @param x int[2]
       @return act int
    """
   
    def act(self, x):      
       f=(x[0]*self.w[1] + x[1]*self.w[2] + self.w[0])
       f=1/(1+m.exp(-f))
       if(f<=0.5):
           return 0
       else:
           return 1
       
    """
    method single_it_train recieves an input point, its label and a learning rate
    to refresh weights to adjust them to desired output
    """
       
    def single_it_train(self, input, label, C):
        
        x= [1, input[0], input[1]]
        
        
        if self.act(input)==1 and label==0:
            #w=w-C*x
            Cx=list(map(lambda x: x * C, x))
            self.w=list(map(operator.sub, self.w, Cx))
        if self.act(input)==0 and label==1:
            #w=w+C*x
            Cx=list(map(lambda x: x * C, x))
            self.w=list(map(operator.add, self.w, Cx))
            
    """
    method single_ep_train recieves all the point XN from data set, its labels YN
    and the learning rate C, to iterate single_it_train over al data set points
    """
    
    def single_ep_train(self, XN, YN, C):
        l=len(YN)
        for i in range(l):
            self.single_it_train(XN[i],YN[i],C)
            
    """
    method train recieves all the point XN from data set, its labels YN,
    the learning rate C and epochs to iterate single_ep_train epoch times.
    This method also records the accuracy before every trainning epoch
    """
            
            
    def train(self, epoch, XN, YN, C):
        for i in range(epoch):
            self.single_ep_train(XN,YN,C)
            self.acc.append(self.accuracy(XN,YN))
            
    """
    method accuracy calculate and returns the number of correct classificationmade by the perceptron
    over the entire dataset XN
    """
    
    def accuracy(self, XN, YN):
        count=0
        for i in range(len(YN)):
            resp=self.act(XN[i])
            if resp==YN[i]:
                count+=1
        acc=count/len(YN)
        return acc    
        


if __name__ == "__main__":
#    main()
    p=Perceptron()
    
    """
    Create data set of 50 random point labeled as 1 if X>=[1,1], and 0 otherwise
    """
    
    ejemplos=50
    X=[]
    Y=[]
    X_1=[]
    X_2=[]
    for i in range(ejemplos):
        Xi=[random.randint(-100,100)/10,random.randint(-100,100)/10]
        if Xi[0]>=1 and Xi[1]>=1:
            Yi=1
        else:
            Yi=0
        Y.append(Yi)
        X.append(Xi)
        X_1.append(Xi[0])
        X_2.append(Xi[1])
        
    #train perceptron for 1000 epochs with 0.001 learning rate
    p.train(1000,X,Y,0.001)
    
    #separete point by label to plot them
    X_1R=[]
    X_2R=[]
    X_1G=[]
    X_2G=[]
    
    for i in range(ejemplos):
        if Y[i]==1:
            X_1R.append(X_1[i])
            X_2R.append(X_2[i])
        else:
            X_1G.append(X_1[i])
            X_2G.append(X_2[i])
            
    
    #plot perceptron accuracy
    t = list(range(len(p.acc)))
    plt.plot(t,p.acc)
    plt.title('Perceptron classification accuracy over epochs')
    plt.show()
    
    #plot data set
    plt.plot(X_1G,X_2G,'go')
    plt.plot(X_1R,X_2R,'ro')
    
    #plot classification frontier
    [b, w1, w2] = p.w
    x = -b / w1
    y = -b / w2

    d = y
    c = -y / x

    line_x_coords = [0, x]
    line_y_coords = list(map(operator.add, list(map(lambda x: x * c, line_x_coords)) , [d,d]))
    
    m=(line_y_coords[0]-line_y_coords[1])/(line_x_coords[0]-line_x_coords[1])
    n=line_y_coords[1]-m*line_x_coords[1]
    p_frontier1=[(10-n)/m,10]
    p_frontier2=[10,10*m+n]
    
    plt.plot([p_frontier1[0],p_frontier2[0]], [p_frontier1[1],p_frontier2[1]],'b')
    plt.title('Perceptron classification')

    #predict=[p.act(X[0]),p.act(X[1]),p.act(X[2]),p.act(X[3]),p.act(X[4]),p.act(X[5])]