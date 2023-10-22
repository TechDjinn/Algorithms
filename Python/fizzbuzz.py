def main():
    fizzbuzz()


def fizzbuzz():
    """
    Description:
        Loop through all numbers 1 <=> 100. 
        If multiple of 3: Print "Fizz"
        If multiple of 5: Print "Buzz"
        If multiple of 15: Print "FizzBuzz"
        Else: Print the number.
        Function takes no argument; and has no return value.
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        

if __name__ == "__main__":
    main()