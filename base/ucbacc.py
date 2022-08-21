from accelerometer import Accelerometer

class UCBAcc(Accelerometer):

    def show_type(self):
        print(f'I am {self.name}, created at UC Berkeley!')


if __name__ == '__main__':
    acc_ucb = UCBAcc('UCBAcc', 'Berkeley', '2019-03-01')
    acc_ucb.show_type()