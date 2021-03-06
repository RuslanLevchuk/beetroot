class Mathematician:
    def square_nums(self, nums):
        return [i*i for i in nums]

    def remove_positives(self, nums):
        return [i for i in nums if i < 0]

    def filter_leaps(self, nums):
        return [i for i in nums if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020, 500, 800]) == [1884, 2020, 800]