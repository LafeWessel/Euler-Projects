# Euler class contains a class that has references to each of the problems and

from EulerProblem import EulerProblem
import Multiples_Three_Five
import Even_Fibonacci

class EulerProject:

    def __init__(self):
        self.problem_list = [
            Multiples_Three_Five.MultiplesThreeFive(),
            Even_Fibonacci.EvenFibonacci()
        ]
    # end def

    def run_problems(self):
        print("Running all problems")
        for p in self.problem_list:
            print(p.run())
        print("Finished all problems")
        return
    # end def
