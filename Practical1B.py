#Name: Deepak Keshri  308/SYIT

X = [[11,7,3],
   [4,5,6],
   [7,8,9]]

Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
        for r in result:
            print(r)
            
#3X3 matrix
X = [[12,7,3],
     [4,5,6],
     [7,8,9]]
#4X4 matrix
Y = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
#itrate through rows of X
for i in range(len(X)):
#itrate through columns of Y
    for j in range(len(Y[0])):
#itrate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
            for r in result:
                print(r)
            
