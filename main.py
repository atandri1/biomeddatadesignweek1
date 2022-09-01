
from scipy.optimize import linear_sum_assignment
import numpy as np

'''
10 doctor,
3 Hospitals,[4,4,4]
'''

def Hungarian(C):
    '''
    C: N*K
    x: (x[0],x[1])
    '''

    # KM algo
    N = C.shape[0] 
    K = C.shape[1]

    LX = np.max(C,axis=0)
    LY = np.zeros((K))
    
    S = [] # X
    T = [] # Y

    match = -np.ones((N)) # index x match value y
    
    AugPath = [[],[]]

    def recur(y):
        if np.any(match==y) == False:
            return y,True
            
        AugPath[0].append(np.where(match==y)[0][0])

        flag_recur = False # indicating having another edge satisfying LX+LY=C
        for y_recure in range(K):
            if y_recure not in AugPath[1] and LX[AugPath[0][-1]]+LY[y_recure] == C[AugPath[0][-1],y_recure]:
                flag_recur = True
                break

        return y_recure,flag_recur

    for x in range(N):
        # add new (x,y)
        flag2 = False
        y_temp = 0
        if np.any(C[x,:]-LY==LX[x]) == False:
            flag2 = False
        else:
            flag2 = True
            y_temp = np.where(C[x,:]-LY==LX[x])[0][0]

        flag = False
        AugPath = [[x],[]] # for (X, Y), X first
        while not flag:
            if y_temp not in T and flag2:
                flag2 = True
                S.append(x)
                T.append(y_temp)
                AugPath[1].append(y_temp)
                for i in range(len(AugPath[0])):
                    match[AugPath[0][i]] = AugPath[1][i]
                flag = True
            else: # conflict
                AugPath[1].append(y_temp)
                y_next = y_temp
                y_temp,flag_recur = recur(y_next)
                while not flag_recur: # no
                    print(AugPath[0])
                    LX[AugPath[0]] = LX[AugPath[0]] - 1
                    LY[AugPath[1]] = LY[AugPath[1]] + 1
                    AugPath[0].pop(-1)
                    y_temp,flag_recur = recur(y_next) 
    
    ans = (list(np.arange(N)),list(match))
    return ans


def main():
    Capacity = np.array([4,1,6])
    position = np.zeros((np.sum(Capacity)))
    prefer = np.array([
        [0,1,2],
        [1,2,0],
        [1,0,2],
        [2,1,0],
        [1,2,0],
        [2,1,0],
        [1,0,2],
        [2,1,0],
        [1,2,0],
        [2,1,0]
        ]
    )

    C = np.zeros((np.shape(prefer)[0],np.sum(Capacity)))
    for i_doc in range(np.shape(prefer)[0]):
        flag = 0
        for i_hos in range(np.shape(prefer)[1]):
            C[i_doc,flag:flag+Capacity[i_hos]] = prefer[i_doc,i_hos]
            flag = flag + Capacity[i_hos]

    flag = 0
    for i_hos in range(np.shape(prefer)[1]):
        position[flag:flag+Capacity[i_hos]] = i_hos
        flag = flag + Capacity[i_hos]

    x = Hungarian(C)
    print(x)
    print(np.array(x[0]).astype(np.int))
    # print(position[0])
    ans = np.array([position[i] for i in np.array(x[1]).astype(np.int)])
    print(ans.astype(np.int))

    print('and')

    xx = linear_sum_assignment(C,True)
    print(xx)
    print(np.array(xx[0]).astype(np.int))
    # print(position[0])
    ans = np.array([position[i] for i in np.array(xx[1]).astype(np.int)])
    print(ans.astype(np.int))

if __name__ == "__main__":
    main()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
