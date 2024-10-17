import numpy as np

list1=[2,3,4,5,6]
list2=[10,20,30,40,50]

vec1=np.array(list1)
vec2=np.array(list2)
print("ASSIGNMENT CHANGES DONE IN MAIN BRANCH ")
vec3=vec1.dot(vec2)
print(vec3)
