#The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


from EulerProblem import EulerProblem

class Largest_Prime_Factor(EulerProblem):

    def __init__(self):
        self.name = "Largest Prime Factor"
        self.result = 0
        self.to_factor = 600851475143

    def run(self):
        prime_factors = []
        i = 2
        k = self.to_factor
        while i <= k :
            # if i is a factor of k
            if k % i == 0:
                #print(i, "divides", k)
                prime_factors.append(i)
                k /= i
            # end if

            # check if close to end
            if i == k:
                prime_factors.append(k)
            # end if


            # increment counter
            i += 1
            # make sure to avoid all evens
            if i % 2 == 0:
                i += 1
            # end if
        # end while
        self.result = prime_factors[-1]
        return
