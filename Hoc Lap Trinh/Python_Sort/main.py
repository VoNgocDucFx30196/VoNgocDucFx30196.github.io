import random
import time

n = [random.randint(0,100) for i in range(1000)]
print(n)
a=0
b=0

def swap(a,b,m):
    temp=m[a]
    m[a]=m[b]
    m[b]=temp

def s_sort(n):
    global a
    a= time.time()
    for i in range(len(n)):
        mn = i
        for j in range(i,len(n)):
            if n[j]<n[mn]:
                mn=j
        swap(mn,i,n)
    a= time.time()-a
def i_sort(n):
    global b
    b=time.time()
    pos=0
    for i in range(1,len(n)):
        pos=i
        while n[pos]<n[pos-1] and pos!=0:
            swap(pos,pos-1,n)
            pos-=1
    b=time.time()-b

i_sort(n)
n = [random.randint(0,100) for i in range(1000)]
s_sort(n)
print(a,b)
print(n)
