from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.__count__ = size
        self.__sum__ = 0
        self.__collection__ = deque()

    def next(self, val: int) -> float:
        self.__sum__ += val
        self.__collection__.append(val)
        count = len(self.__collection__)
        while count > self.__count__:
            del_val = self.__collection__.popleft()
            self.__sum__ -= del_val
            count -= 1
        return self.__sum__ / count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
def main():
    ma = MovingAverage(3)
    inputs = [1, 10, 3, 5]
    for  val in inputs:
        print( ma.next(val))

if __name__ == "__main__":
    main()