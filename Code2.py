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
            return a
       else :
          while b != 0: #the loop continues until the second number becomes zero
               x = a % b #calculating the remainder of number a with b
               a = b
               b = x #giving b the value of remainder
       return a
    #this function calls input function and then calls GCD function to perform Euclidean alogorithm
    # on numbers and prints an output statement
    def display (self):
        a,b = self.inputs()
        print(f"The GCD of {a} and {b} is {self.GCD(a,b)}")
    #this function takes input from user
    def inputs(self):
        a = -1
        while a < 0: #repeatedly asks user to enter a number until it enters a positive number
            a = int(input("Enter the first positive number: "))
            if a < 0:
                print("Invalid input. Please enter a positive number.")
        b = -1
        while b < 0: #same for the second number , this ensures that the program always returns a positive number
            b = int(input("Enter the second positive number: "))
            if b < 0:
                print("Invalid input. Please enter a positive number.")
        return a, b
def main():
    A = EuclideanAlgorithm()
    A.display()
if __name__ == "__main__":
  main()
