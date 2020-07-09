import numpy as np
import random as random
import matplotlib.pyplot as plt
import time

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

def nearestPairRabin(S):
    S1 = picking(S)
    # Bestimmen von delta(S1) mit dem gleichen Algorithmus, allerdings interessiert hier das Paar noch nicht
    S2 = picking(S1)
    deltaS2 = nearestPairBF(S2)[0]
    L1s2 = decomposition(2 * deltaS2, S1) # doppelte Weite
    mindistS2 = deltaS2
    npair = []
    for j in range(len(L1s2)):
        dist, pair = nearestPairBF(L1s2[j])
        if dist < mindistS2:
            mindistS2 = dist
            npair = pair
    deltaS1 = mindistS2
    # berechnung von delta(S1), noch BF(S1)
    # deltaS2 = nearestPairBF(S2)[0]
    # calculate delta(S1) = min(d(x,y)) x,y in S1 in O(n)
    # temporär BF
    
    # gamma mit delta = delta(S1) & gamma1-gamma4 mit 2delta, um konstruiert, sodass nur ein Gamma nötig ist
    L1 = decomposition(2*deltaS1, S) # gleiches, bloß nach rechts doppelte Weite
    mindist = deltaS1
    nearpair = npair
    # durchsuchen der Quadrate nach geringster Distanz
    for j in range(len(L1)):
        if len(L1[j]) > 1:
            dist, pair = nearestPairBF(L1[j])
            if dist < mindist:
                mindist = dist
                nearpair = pair
    return nearpair, mindist

# Erstellung der Dekomposition nach Gamma, nicht Beachtung, dass Punkte zu mehreren Teilmengen gehören können (potentielle Fehlerquelle!)
def decomposition(delta, s):
    decomp = []
    Stemp = sorted(s) # rewrite sorted
    temp = []
    calc = []
    for x in Stemp:
        ai = x[0]//delta
        bi = x[1]//delta
        calc.append((ai,bi))
    j = 0
    while j < len(calc):
        while hash(calc[j-1]) == hash(calc[j]) and j < len(calc):
            temp.append(Stemp[j])
            if Stemp[j-1] not in temp : temp.append(Stemp[j-1])
            j += 1
        if temp != [] :
            decomp.append(temp)
            temp = []
        else:
            j += 1

    return decomp
    
# picking a subset Si from S, so c(Si) = len(S)**(2/3)
def picking(s):
    m = len(s) ** (2 / 3)
    s1 = []
    # picking S1
    while len(s1) < m:
        i = random.randrange(len(s))
        # can be done more efficient by hashing (due to iteration on indizes)
        if s[i] not in s1: s1.append(s[i])
    return s1
# distance computation in R^2
def distance(x,y):
    return np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

if __name__ == '__main__':
    #Set = [(0,2), (10,10), (3.85, 5.2),(10.3,7), (9.7, 3.9), (4.2, 5.3), (7.8, 9), (6,7), (8,1), (10, 0.1), (2, 11), (1.5, 8), (7.5, 6), (8, 4.2), (5,9), (6, 0.5), (0.1, 0.2), (0.7, 0.7),(2,1),(3,1),(5,5),(1,0.5), (1,3), (0.5,0.5), (3,3), (2,5), (4,4), (4,5), (3,4), (1,2), (3,2)]
    # Generate Randomset
    randSet = []
    #random.seed()
    for i in range(10000):
        x=random.uniform(1,30)
        y=random.uniform(1,30)
        randSet.append((x,y))
    #random.seed()

    print("Length of Set:", len(randSet))
    tbf = time.process_time()
    d, p = nearestPairBF(randSet)
    elapsed_time_bf = time.process_time()-tbf
    print("Brute Force:")
    print("nearest Pair random S:", p)
    print("distance of nearest Pair in random S:", d)
    print("Time in sec:", elapsed_time_bf)

    timerab = time.process_time()
    p, d = nearestPairRabin(randSet)
    elapsed_time_rab = time.process_time()-timerab

    print("Rabin:")
    print("nearest Pair random S:", p)
    print("distance of nearest Pair in random S:", d)
    print("Time in sec:", elapsed_time_rab)
