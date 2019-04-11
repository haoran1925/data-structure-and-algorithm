############
###### 04/11/2019
###### Given a set of n distinct points in the plane, find every (maximal) line segment that connects a subset of 4 or more of the points.
###### Task: http://coursera.cs.princeton.edu/algs4/assignments/collinear.html


import matplotlib
import numpy as numpy
matplotlib.use("Agg")
import matplotlib.pyplot as plt


### Read text and get the points
def read_txt(dir,filename):
	file_path = dir+filename
	f = open(file_path, 'r')
	data = f.readlines()
	return data

dir = '/Users/tianma/Desktop/Python/dsa/pattern/'
filename = 'input8.txt'
data = read_txt(dir,filename)


### Get coordinates
x,y=[],[]
for eachline in data:
	element= eachline.split()   # split(',') set parameter by yourself
	x.append(float(element[0]))
	y.append(float(element[1]))
points = (x,y)


### Plot points
fig = plt.figure()
plt.scatter(x,y)



### Search for points in the same line
slope_set = []
slope_index_count =[]
count = 0 
for i in range(len(x)):
	for j in range(i+1,len(x)):
		vertical_count = 0
		if x[i]-x[j]!=0:
			slope = (y[i]-y[j])/(x[i]-x[j])
			if slope not in slope_set:
				slope_set.append(slope)
				slope_index_count.append(1)
			else: 
				slope_index_count[slope_set.index(slope)] += 1
				if slope_index_count[slope_set.index(slope)] ==3:
					count +=1
					x_vals = [x[i],x[j]]
					y_vals = [y[i],y[j]]
					plt.plot(x_vals, y_vals, '--')
		elif x[i]-x[j]==0:
			vertical_count +=1
			if vertical_count ==3:
				count +=1
				x_vals = [x[i],x[j]]
				y_vals = [y[i],y[j]]
				plt.plot(x_vals, y_vals, '--')

print ('There are {} lines'.format(count))
plt.savefig('{}pattern.png'.format(dir))


			


		











