#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from EulerProblem import EulerProblem

class Smallest_Multiple(EulerProblem):

    def __init__(self):
        self.name = "Smallest Multiple"
        self.result = 0
        self.target_num = 20

    def run(self):
        hasEven = False
        factors = [t for t in range(2, self.target_num + 1)]
        f_dict = {}
        primes = {}
        # get factors and set of all primes
        for t in factors:
            f_dict[t] = self.find_factors(num=t)

            for d in f_dict[t]:
                primes[d] = 0
            # end for
        # end for

        # find highest count of each prime factor
        for p in primes.keys():
            top = 0
            # look through each factored number
            for f in f_dict.keys():
                ct = 0
                # look through factors of each number
                for d in f_dict[f]:
                    if p == d:
                        ct += 1
                    # end if
                # end for
                if ct > top:
                    top = ct
                # end if
            # end for
            primes[p] = top
        # end for

        self.result = 1
        for k,v in primes.items():
            self.result *= (k**v)


    def find_factors(self, num: int):
        factor_list = []
        i = 2
        while i <= num:
            while num % i == 0:
                factor_list.append(i)
                num /= i
            # end while
            i += 1
            # end if else
        # end while
        return factor_list
