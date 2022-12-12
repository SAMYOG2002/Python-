mat_a = [[1,2,3,],
         [4,5,6],
         [7,8,9]]
mat_b = [[2,4,1],
         [6,4,1],
         [2,5,8]]
result = [[0,0,0],[0,0,0],[0,0,0]]
r1 = len(mat_a)
c1 = len(mat_a[0])
r2 = len(mat_b)
c2 = len(mat_b[0])
if not(c1==r2):
    print("Matrix cannot be multiplied")
else:
    for i in range(r1):
        for j in range(c1):
             for k in range(r2):
                 result[i][j] += mat_a[i][k] * mat_b[k][j]




for r in result:
    print(r)
    







