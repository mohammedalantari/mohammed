#the class that contains function to preform Euclidean Algoritm on two numbers
class EuclideanAlgorithm:
    def __init__(self):
        pass
    # this function calculates the Greatest Common Divisor of two numbers via Euclidean Algorithm
    # this function has two parameters - a and b ; two positive integers
    # this functions returns the GCD of a and b
    # this algoritms finds hte gcd of two number s by repetedly dividing the first number with the remiander of the
    # prevoius division until the remianer becomes zero
    def GCD (self,a,b):
       if (a==0):
            return b
       elif (b==0):
             return b
      else :
          while b != 0: #the loop continues until the second number becomes zero
              x = a % b #calculating the remainder of number a with b
              a = b
              b = x #giving b the value of remainder
     return a
    #this function takes two pramaters a and b and calls GCD function to perform Euclidean alogorithm
    # on numbers and prints an output statement
    def display (self,a,b):
        print(f"The GCD of {a} and {b} is {self.GCD(a,b)}")
def main():
    A = EuclideanAlgorithm()
    A.display(4,8)

if __name__ == "__main__":
  main()
