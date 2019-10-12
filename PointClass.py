import math


class PointClass:
    """
    Represent the poing in two dimentional geometric co-ordinates
    """

    def __init__(self,x=0,y=0):
        """
        Initialize the object .
        :param x:
        :param y:
        """
        self.x=x
        self.y=y

    def reset(self):
        """
        Reset the point values to zero
        :return:
        """
        self.x=0
        self.y=0

    def move(self,x,y):
        self.x=x
        self.y=y

    def calculate_distance(self,p2):
        """
        Calculate the distance between two points using the
        ecuclidian distance formula
        :param p2: another point to fine distance
        :return: double type distnace value
        """
        return math.sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2)

    def display(self):
        print(self.x,self.y)
    #pass


def main():
    p = PointClass(0, 0)
    p2 = PointClass(2, 2)
    p3 = PointClass(2)
    print(p)
    print(p2)
    p.display()
    p2.display()
    p3.display()


if __name__ == '__main__':
    main()




# p.reset();
# print(p.x,p.y)
# p2.move(2,0)
# print(p.x,p.y)
# assert (p.calculate_distance(p2)==p2.calculate_distance(p))
# print(p.calculate_distance(p2))
