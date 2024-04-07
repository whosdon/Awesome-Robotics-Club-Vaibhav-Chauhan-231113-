import cv2
import numpy as np

img = cv2.imread("image2.png")
img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imwrite("filtered_noise.png", img)

x=img.shape[1]
y=img.shape[0]
black_threshhold = 80
blue_threshhold = 150
xs = []
ys = []
final = []



for i in range (y):
    avg = np.zeros((3,))
    for j in range (x):
        avg+=img[i][j]/x
    if np.average(avg)<black_threshhold:
        ys.append(i)
        for j in range (x):
            img[i][j] = [0, 0 ,0]

for i in range (x):
    avg = np.zeros((3,))
    for j in range(y):
        avg+=img[j][i]/y
    if np.average(avg) < black_threshhold:
        xs.append(i)
        for j in range (y):
            img[j][i] = [0, 0 ,0]


collumns = len(xs)-1
rows = len(ys) - 1

for i in range(rows):
    arr = []
    for j in range(collumns):
        avg = np.zeros((3,))
        for a in range(ys[i]+1, ys[i+1]):
            for b in range(xs[j]+1, xs[j+1]):
                avg += img[a][b]/((ys[i+1]-ys[i]-1)*(xs[j+1]-xs[j]-1))
        if avg[0]>blue_threshhold:
            arr.append(1)
        else:
            arr.append(0)
        for a in range(ys[i]+1, ys[i+1]):
            for b in range(xs[j]+1, xs[j+1]):
                if arr[-1] == 1: 
                    img[a][b] = [255, 0, 0]
                else:
                    img[a][b] = [0, 255, 255]
    final.append(arr)

visited = [[-1 for i in range(collumns)] for j in range(rows)]
parent = [[(-1,-1) for i in range(collumns)] for j in range(rows)]

visited[0][0] = 0
arr = [(0,0)]

while(len(arr)!=0):
    t = arr[0]
    ts = []
    ts.append((t[0]+0, t[1]+1))
    ts.append((t[0]+1, t[1]+0))
    ts.append((t[0]+0, t[1]+-1))
    ts.append((t[0]+-1, t[1]+0))

    for ti in ts:
        if ti[0] >= 0 and ti[0] < rows and ti[1]>=0 and ti[1]<collumns and final[ti[0]][ti[1]]==0 and visited[ti[0]][ti[1]] == -1:
            visited[ti[0]][ti[1]] = visited[t[0]][t[1]]+1
            parent[ti[0]][ti[1]] = t
            arr.append(ti)

    del arr[0]

next = ()
to_print = [(rows-1, collumns-1)]
while(next!=(0,0)):
    next = parent[to_print[0][0]][to_print[0][1]]
    to_print = [next, ] + to_print

print(to_print)

for i in range(len(to_print)-1):
    start = to_print[i]
    end = to_print[i+1]

    startp = ((int)((ys[start[0]]+ys[start[0]+1])/2), (int)((xs[start[1]]+xs[start[1]+1])/2))
    endp = ((int)((ys[end[0]]+ys[end[0]+1])/2), (int)((xs[end[1]]+xs[end[1]+1])/2))
    
    for a in range(min(startp[0], endp[0]+1),max(startp[0], endp[0]+1)):
        for b in range(min(startp[1], endp[1]+1), max(startp[1], endp[1]+1)):
            img[a][b] = [0,0,255]

cv2.imwrite("answer.png", img)
