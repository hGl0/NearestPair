import numpy as np
# brute force approach

def nearestPairBF(S):
    mindist = np.inf
    Pair = []
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            dist = distance(S[i], S[j])
            if mindist > dist:
                mindist = dist
                Pair = [S[i], S[j]]
    return mindist, Pair


def distance(x,y):
    return np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

if __name__ == '__main__':
    S = [(0,2), (1,0.5), (1,3), (2,5), (5,5), (4,4), (4,5), (3,4)]
    print(nearestPairBF(S))
