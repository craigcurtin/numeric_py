import numpy as np
from sensor import Sensor

if __name__ == '__main__':
    sensor1 = Sensor('sensor1', 'Berkeley', '2019-01-01')
    data = np.random.randint(-10, 10, 10)
    sensor1.add_data(np.arange(10), data)
    sensor1.data