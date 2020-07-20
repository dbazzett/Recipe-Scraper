# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:00:53 2020

@author: me442
"""
class recipe:
  def __init__(self):
    self.recipeList = []
  def addItem(self,recipeItem):
    self.recipeList.append(recipeItem)
  def removeItem(self,item):
    self.recipeList.remove(item)
  def __repr__(self):
    return self.recipeList
  
class recipeItem:
  def __init__(self, inputQuantity, unit, ingredient):
    self.unit = unit.lower()
    self.ingredient = ingredient.lower() 
    if(self.isFraction(inputQuantity)):
      self.quant = fraction(inputQuantity[0],inputQuantity[2])
      self.strRep= str(self.quant.num)+'/' +str(self.quant.den) + ' '+ self.unit + ' '+ self.ingredient
    else:
      self.quant = float(inputQuantity)
      self.strRep = str(self.quant) + ' '+ self.unit + ' '+ self.ingredient
  def isFraction(self,inputQuantity):
    slash1 = '\\'
    slash2='/'
    if(slash1 in inputQuantity or slash2 in inputQuantity):
      return True
    else:
      return False
  def __repr__(self):
    return self.strRep

class quantity:
  def __init__(self,qty):
    self.value = qty
class fraction:
  def __init__(self, numerator,denominator):
    self.num = int(numerator)
    self.den = int(denominator)
    self.value = self.num/self.den
    



r1 = recipe()
r1i1 = recipeItem('1/2','cup','Flour')
r1i2 = recipeItem('3','cup','sugar')
r1i3 = recipeItem('1/4','cup','cinamon')
r1.addItem(r1i1)
r1.addItem(r1i2)
r1.addItem(r1i3)

for i in range(len(r1.recipeList)):
  print(r1.recipeList[i])
