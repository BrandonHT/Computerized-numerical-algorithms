# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 00:27:23 2020

@author: brand
"""

import random
from sklearn import model_selection

datos=open('SSAMP300.XLS','r')
datosTuplas=datos.readlines()
random.shuffle(datosTuplas)

train,test=model_selection.train_test_split(datosTuplas,test_size=0.2)

trainFile=open("customTrain.xls","w")
trainFile.write("".join(train))
trainFile.close()

testFile=open("customTest.xls","w")
testFile.write("".join(test))
testFile.close()