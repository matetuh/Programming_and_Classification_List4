import nltk
import numpy as np
import random
#import books from nltk.books
from nltk.book import text1, text2, text3

def Jacard_similarity_min(A, B):
    licz = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            licz = licz + 1
    return licz/(len(A))

def set_sum(A,B):
    return A+B

def set_il(A,B):
    a_set = set(A) 
    b_set = set(B) 
    c_set = set()
    if (a_set & b_set):
        c_set = c_set | (a_set & b_set)
    return list(c_set)
        
def Jaccard_similarity(A,B):
    len_set_AuB = len(set_sum(A, B))
    len_set_AnB = len(set_il(A, B))
    return len_set_AnB/len_set_AuB

#import text 1
text_1=[x.lower() for x in text1]

#import text 2
text_2=[x.lower() for x in text2]

#import text 3
text_3=[x.lower() for x in text3]

S11={x:len(x) for x in set(text_1)}
S22={x:len(x) for x in set(text_2)}
S33={x:len(x) for x in set(text_3)}

S1_max=set(sorted(S11.items(), reverse=True, key=lambda x : x[1]))
S2_max=set(sorted(S22.items(), reverse=True, key=lambda x : x[1]))
S3_max=set(sorted(S33.items(), reverse=True, key=lambda x : x[1]))

S1 = []
S2 = []
S3 = []
S4 = []

col1 = []
col2 = []
col3 = []

for (w,l) in S1_max:
    if l < 8:
        S1.append((w,l))

for (w,l) in S2_max:
    if l < 8:
        S2.append((w,l))

for (w,l) in S3_max:
    if l < 8:
        S3.append((w,l))

J12 = Jaccard_similarity(S1,S2)
J23 = Jaccard_similarity(S2,S3)
J13 = Jaccard_similarity(S1,S3)

S1 = S1[:100]
S2 = S2[:100]
S3 = S3[:100]

for elem in S1:
    S4.append(elem)
for elem in S2:
    S4.append(elem)
for elem in S3:
    S4.append(elem)

for (w,l) in S4:
    if (w,l) in S1:
        col1.append(1)
    else:
        col1.append(0)
for (w,l) in S4:
    if (w,l) in S2:
        col2.append(1)
    else:
        col2.append(0)
for (w,l) in S4:
    if (w,l) in S3:
        col3.append(1)
    else:
        col3.append(0)

S_S1 = []
S_S2 = []
S_S3 = []

for i in range(100):
    col1 = np.random.permutation(col1)
    for j in range(len(col1)):
        if col1[j] == 1:
            S_S1.append(j)
            break
    col2 = np.random.permutation(col2)
    for j in range(len(col1)):
        if col2[j] == 1:
            S_S2.append(j)
            break
    col3 = np.random.permutation(col3)
    for j in range(len(col1)):
        if col3[j] == 1:
            S_S3.append(j)
            break

print("Jacard Similarity (minhashes) : S1 and S2: ", Jacard_similarity_min(S_S1, S_S2))
print("Jacard Similarity (minhashes) : S2 and S3: ", Jacard_similarity_min(S_S2, S_S3))
print("Jacard Similarity (minhashes) : S1 and S3: ", Jacard_similarity_min(S_S1, S_S3))

print("Jacard Similarity : S1 and S2: ", J12)
print("Jacard Similarity : S2 and S3: ", J23)
print("Jacard Similarity : S1 and S3: ", J13)
