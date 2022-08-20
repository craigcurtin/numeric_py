import numpy as np
from numpy.linalg import eig



if __name__ == '__main__':
    a = np.array([[0, 2],
                  [2, 3]])
    w,v=eig(a)
    print('E-value:', w)
    print('E-vector', v)