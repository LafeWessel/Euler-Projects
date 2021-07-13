# Instructions:L
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from EulerProblem import EulerProblem


class MultiplesThreeFive(EulerProblem):

    def __init__(self):
        self.name = "Multiples of 3 and 5"
        self.result = 0
    # end def

    def run(self):
        print("Running", self.name)
        # calculate factors
        f_three = self.find_factors(factor = 3, max_bound = 1000)
        f_five = self.find_factors(factor = 5, max_bound = 1000)

        # remove duplicate factors
        factors = set(f_three)
        factors = factors.union(f_five)

        # sum factors
        self.result = sum(factors)
        return self.result
    # end def

    # find factors of factor between min and max
    def find_factors(self, factor: int, max_bound: int, min_bound = 0):
        factors = []

        for i in range(min_bound, max_bound):
            if i % factor == 0:
                factors.append(i)
            # end if
        # end for
        return factors
    # end def

