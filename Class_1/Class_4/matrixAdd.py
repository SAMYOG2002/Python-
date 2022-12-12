mat_a = [[1,2,3],
         [4,5,6],
         [7,8,9]]

mat_b = [[2,4,1],
         [6,4,1],
         [2,5,8]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
          
r1 = len(mat_a)
c1 = len(mat_a[0])
for i in range(r1):
    for j in range(c1):
            result[i][j] = mat_a[i][j] + mat_b[i][j]
for r in result:
    print(r)


