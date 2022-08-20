from numpy.linalg import inv




def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

if __name__ == '__main__':
    a_inv = inv(a)

    for i in range(8):
        x = np.dot(a_inv, x)
        lambda_1, x = normalize(x)

    print('Eigenvalue:', lambda_1)
    print('Eigenvector:', x)