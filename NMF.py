import numpy as np
import numpy.matlib
import math
from numpy import linalg as LA
import random
m=input("enter no of rows in matrix V:")
n=input("enter no of columns in matrix V:")
v=[[random.random() for col in range(n)] for row in range(m)]
for i in range(m):
	for j in range(n):
		v[i][j]=input()
	print
r=input()
w=np.random.rand(m,r)
h=np.random.rand(r,n)
print("the w matrix is:")
print w
print("the h matrix is:")
print h
g=np.dot(w.transpose(),v)
e=np.dot(w.transpose(),w)
print g
print e
'''f=np.dot(e,h)
j=np.true_divide(g,f)
l=np.multiply(h,j)
print("update h")
print l
a=np.dot(v,h.transpose())
b=np.dot(w,h)
c=np.dot(b,h.transpose())
d=np.true_divide(a,c)
p=np.multiply(w,d)
print("update w")
print p
t=np.dot(p,l)
s=v-t
print("s matrix")
print s
u=LA.norm(s)
print("euclideannorm is:")
print u
if(u>=0.01):
       while(u>=0.01):
	g=np.dot(w.transpose(),v)
	e=np.dot(w.transpose(),w)
	f=np.dot(e,h)
	j=np.true_divide(g,f)
	l=np.multiply(h,j)
	h=l
#	print("update h is")
	print l
	a=np.dot(v,h.transpose())
	b=np.dot(w,h)
	c=np.dot(b,h.transpose())
	d=np.true_divide(a,c)
	p=np.multiply(w,d)
	w=p
#	print("update w is")
	print p
	t=np.dot(w,h)
	s=v-t
	print("s matrix")
	print s
	y=LA.norm(s)
	print y
else:                    
	print("update w:")
	print p
	print("update h:")
	print l
	print("updated wh:")
	print np.dot(p,l)'''