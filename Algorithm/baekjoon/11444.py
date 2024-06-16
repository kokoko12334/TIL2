def cal(m1, m2):
    new = [[0,0],[0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j] += m1[i][k] * m2[k][j]
            
            new[i][j] = new[i][j] % 1000000007
    return new     


def div(matrix, exp):

    if exp == 1:
        return matrix
    
    tmp = div(matrix, exp//2)
    
    if exp % 2 == 1:
        return cal( cal(tmp, tmp), [[1,1],[1,0]])
    else:
        return cal(tmp, tmp)


n = int(input())

if n == 1:
    print(1)

else:

    matrix = div([[1,1],[1,0]],n-1)

    print(matrix[0][0])
    