# Task 2: Write a program to perform matrix multiplication for two given matrices.
def matrix_mul(x,y):

    rows_x = len(x)
    cols_x = len(x[0])
    rows_y = len(y)
    cols_y = len(y[0])

    if cols_x != rows_y:
        raise ValueError("Number of columns in A must equal number of rows in B")
    # initialize the result matrix with zeros
    result = [[0 for _ in range(cols_y)] for _ in range(rows_x)]

    for i in range(rows_x):
        for j in range(cols_y):
            for k in range(cols_x):
                result[i][j] += x[i][k]*y[k][j]
    return result

x =[
    [2,3,4],
    [4,5,6],
    [7,8,9]
]
y=[
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

result = matrix_mul(x,y)
print("THE RESULTANT MATRIX IS :")
for row in result:
    print(row)