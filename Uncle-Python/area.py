from selectors import SelectorKey

from numpy import square


class Square:
    def __init__(self,length):
        self.length = length

    def calculate(self):
        return self.length*self.length

class Cube(Square):
    def __init__(self,length):
        super().__init__(length)

    def calculate(self):
        return super().calculate()*self.length

if __name__ == '__main__':
    square = Square(5)
    print(f'area = {square.calculate()} m**2')

    cube = Cube(10)
    print(f'volume = {cube.calculate()} m**3')
