###############################################################
###### AUTOMATED MARKET OPENING SCHEDULER DURING COVID19 ######
###############################################################

import sys
# import time
# t1 = time.process_time()
def input_values(data):
    '''
    function which takes data provided by the user and returns the values of all parameters such as k, m t, c,
    distances matrix and totla no of shops(K)
    '''
    data = (data.split())
    # print(data,"\n")
    k = int(data[0])       # types of shops opening in one time slot in one market
    m = int((data[1]))     # number of parallel markets
    t = int(data[2])       # number of time slots
    c = float(data[3])     # trade-off constant
    dis = list(map(float, data[4:]))
    # print(dis)
    x=0
    N = k*m*t
    distances = []
    for i in range(N):
        list1 = []
        for j in range(N):
            list1.append(dis[x])
            # if (i!=j):
            #     similarity_val[i][j]=round(1-float(list1[j]),1)
            # # elif(i==j):
            #     list_sim.append(float(0.0))
            x+=1
            # print(list1)
        distances.append(list1)

    # print(distances)
    return k, m, t, c, distances, N

# Reading Input from User
k, m, t, c, distances, N = input_values(sys.stdin.read())
# k, m, t, c, distances, N = input_values((input()))

# print(distances)
# print(similarity_val)

kt = k*t
schedule = [[0 for i in range(kt)] for j in range(m)]


goodness_val = 0

##First schedule
sc=0
sh=[0] #index of shops to be opened
for i in range(1,kt):
    list=distances[N-1]

    list1 = list
    for j in range(N):
        if(j not in sh):
            list1[j]=round(list[j]+1-distances[0][j],1)
    # print(list1, list)
    ind=None

    #maximum= max(list)
    ind=list1.index(max(list))
    # print(ind)
    list[ind]=0
    #print(ind)
    schedule[sc][i] = ind
    sh.append(ind)
    #reduce remaining sessions by 1
sc+=1

# print(sh)
##schedules between first and last schedule
while(sc<k-1):
    d=[0 for x in range(N)]
    for j in range(N):
        if j not in sh:
            d[j]=d[j]+distances[schedule[0][0]][j]
    ind = None
    ind=d.index(max(d))
    schedule[sc][0]=ind
    sh.append(ind)
    for i in range(1, kt):
        # max=gvalue
        list=[0 for x in range(N)]
        for j in range(N):
            if (j not in sh):
                list[j] = round(list[j] + 1 - distances[schedule[sc][0]][j], 1)
        # print(list)
        ind = None

        # maximum= max(list)
        ind = list.index(max(list))
        list[ind] = 0
        # print(ind)
        schedule[sc][i] = ind
        sh.append(ind)
    sc+=1


##last schedule
j=0
while(j<len(schedule[0])):
    for i in range(N):
        if(i not in sh):
            schedule[sc][j]=i
            j += 1
            sh.append(i)
            break

# print(schedule)
# arranging shops in schedules
for i in range(k):
    schedule[i].sort()
# print(schedule)
# arranging in time slots and giving output
for i in  range(len(schedule)):
    m=0
    for j in range(t):
        for x in range(k):
            print(schedule[i][m]+1,end=' ')
            m+=1
        if(j<t-1):
            print("| ",end='')
    print("")
