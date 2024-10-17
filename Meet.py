import numpy as np

list1=[3,4,5,6]
# This line is changed
list2=[10,20,30,40,50]
print("Hello")
vec1=np.array(list1)
vec2=np.array(list2)

vec3=vec1.dot(vec2)
print(vec3)
