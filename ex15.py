# ============================  __eq__, __ne__, __lt__, __le__, __gt__, __ge__  =============================
# __eq__ - ==
# __ne__ - !=
# __lt__ - <
# __le__ - <=
# __gt__ - >
# __ge__ - >=

class Clock:
    __DAY = 86400

    def __init__(self, seconds):
        if not isinstance(seconds, int):
            raise TypeError('second must be int')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('right opperad must be int or Clock')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        return self.seconds == self.__verify_data(other)

    def __lt__(self, other):
        return self.seconds < self.__verify_data(other)

    def __le__(self, other):
        return self.seconds <= self.__verify_data(other)


c1 = Clock(1000)
c2 = Clock(10020)
print(c1 == c2)
print(c1 != c2)  # Эквивалентно not(c1 == c2)
print(c1 < c2)
print(c1 > c2)  # Эквивалентно (c2 < c1)
print(c1 <= c2)
print(c1 >= c2)  # Эквивалентно  (c2 <= c1)
