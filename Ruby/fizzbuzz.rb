def main
    fizzbuzz()
end

def fizzbuzz
    # Description:
    # Loop through all numbers 1 <=> 100.
    # If multiple of 3: Print "Fizz"
    # If multiple of 5: Print "Buzz"
    # If multiple of 15: Print "FizzBuzz"
    # Else: Prints the number.
    # Function takes no argument and has no return value.

    for i in 1..100
        if i % 15 == 0
            puts "FizzBuzz!"
        elsif i % 3 == 0
            puts "Fizz"
        elsif i % 5 == 0
            puts "Buzz"
        else
            puts i
        end
    end
end

main()