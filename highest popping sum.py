#Given a list of numbers,
#find the max sum of k elements
#That can only be "popped" from either end of the list


i=int(input())
m = input().split()
hprack = [int(a) for a in m]
k = int(input())
maxsum=0


for j in range(k+1):
    if j >0:
        currsum = sum(hprack[0:k-j])+sum(hprack[-j:])
    else:
        currsum = sum(hprack[0:k-j])
    #print(hprack[0:k-j],hprack[-j:])
    #print(currsum)
    if currsum > maxsum:
        maxsum = currsum

print(maxsum)