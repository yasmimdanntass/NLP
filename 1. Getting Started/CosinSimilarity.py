import math
import matplotlib.pyplot as plt

def length(doc1): #Getting the length of the vector
    length = 0
    for i in range(len(doc1)):
        length += math.pow(doc1[i],2)
    return math.sqrt(length)

def dot_product(query, doc1): 
    sum = 0
    for i in range(0, len(query)):
        sum += query[i] * doc1[i]
    return sum

def cosin(query, doc1): # Getting the cosin of it 
    cosin = dot_product(query, doc1) / (length(query)*length(doc1))
    return cosin

#Setting up our vectores
query = [1, 1]
A = [4, 3]
B = [5, 5]
C = [1, 10]

#Calculating the cosin between the vectors
print(cosin(A, B))
print(cosin(A, C))
print(cosin(B, C))

#Plotting up our graphic

plt.quiver(0, 0, query[0], query[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Query')
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='red', label='A')
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='green', label='B')
plt.quiver(0, 0, C[0], C[1], angles='xy', scale_units='xy', scale=1, color='orange', label='C')

plt.xlim(-1, 12)
plt.ylim(-1, 12)
plt.axhline(0, color='black', linewidth=0.5)  
plt.axvline(0, color='black', linewidth=0.5)  
plt.gca().set_aspect('equal', adjustable='box')  
plt.grid()
plt.legend()
plt.title("Vectors")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
