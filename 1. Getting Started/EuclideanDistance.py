import math
def doc_length(query, doc1):
    length = 0
    for i in range(0, len(query)):
        length += math.pow(doc1[i] - query[i], 2) #For each dimension, do the operations.

    return math.sqrt(length)

def dot_product(query, doc1):
    sum = 0
    for i in range(0, len(query)):
        sum += query[i] * doc1[i]
    return sum

def cosin(query, doc1):
    cosin = dot_product(query, doc1) / (doc_length(query)*doc_length(doc1))
    return cosin

query = [1, 1]
A = [4, 3]
B = [5, 5]
C = [1, 10]

print(cosin(A, B))
print(cosin(A, C))
print(cosin(B, C))
