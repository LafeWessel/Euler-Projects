#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from EulerProblem import EulerProblem

class Largest_Palindrome_Product(EulerProblem):

    def __init__(self):
        self.name = "Largest Palindrome Product"
        self.result = 0

    def run(self):
        upper_bound = 999
        lower_bound = 0
        i = upper_bound
        # subtract one from one side until it is a palindrome, found lower bound for the numbers
        while not self.check_palindrome(i * upper_bound):
            i -= 1
        # end while
        lower_bound = i
        palindromes = [i*upper_bound]

        # check all number combinations between lower and upper bounds
        for i in range(upper_bound - lower_bound):
            for j in range (upper_bound - lower_bound):
                if self.check_palindrome((lower_bound+i)*(lower_bound+j)):
                    palindromes.append((lower_bound+i)*(lower_bound+j))
                # end if
            # end for
        # end for

        palindromes.sort()
        self.result = palindromes[-1]
        return




    # returns if a given integer `num` is a palindrome
    def check_palindrome(self, num : int):
        k = str(num)
        for i in range(int(len(k) / 2)) :
            if k[i] != k[-(i+1)]:
                return False
            # end if
        # end for
        return True
