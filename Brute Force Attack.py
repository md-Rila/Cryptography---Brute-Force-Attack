# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:03:29 2021

@author: md_Rila_
"""

alpha=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
a=input("Enter the word to be decrypted  :")
a=a.upper()
a=list(a)
print("The Brute Force results are :")
print("\n")
for i in range(1,26,1):
    for j in range(0,len(a),1):
        print(alpha[(alpha.index(a[j])-i)%26],end='')
    print("\n")