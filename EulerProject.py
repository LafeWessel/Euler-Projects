# Euler class contains a class that has references to each of the problems and

from Problems import LargestPrimeFactor, EvenFibonacci, LargestPalindromeProduct, MultiplesThreeFive, SmallestMultiple

# TODO: create way to save results to file then only perform the tests that have no correct answer

class EulerProject:

    def __init__(self):
        self.problem_list = [
            MultiplesThreeFive.Multiples_Three_Five(),
            EvenFibonacci.Even_Fibonacci(),
            LargestPrimeFactor.Largest_Prime_Factor(),
            LargestPalindromeProduct.Largest_Palindrome_Product(),
            SmallestMultiple.Smallest_Multiple()
        ]
    # end def

    def run_problems(self):
        print("Running all problems")
        for p in self.problem_list:
            print("Running", p.name)
            p.run()
            print(p.result)
        print("Finished all problems")
        return
    # end def
