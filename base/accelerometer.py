from sensor import Sensor
import numpy as np

class Accelerometer(Sensor):

    def show_type(self):
        print('I am an accelerometer!')


if __name__ == '__main__':
    acc = Accelerometer('acc1', 'Oakland', '2019-02-01')
    acc.show_type()
    data = np.random.randint(-10, 10, 10)
    acc.add_data(np.arange(10), data)
    acc.data