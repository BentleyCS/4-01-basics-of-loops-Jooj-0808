#All questions must use a loop for full points.
import random

def oddNumbers(n:int) ->str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
    if n < 1:
        return ""

    result = []
    for i in range(1, n + 1, 2):
        result.append(str(i))

    return " ".join(result)

def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    if n >= 1:
        # Generate a range from n down to 1, with a step of -1
        # range(start, stop, step): stop is exclusive, so we go down to 0
        numbers = range(n, 0, -1)
        # Join the string representations of the numbers with spaces
        result = " ".join(str(i) for i in numbers)
        return result
    else:
        result = ""
        return result


def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    number = 1
    cycles = 0

    while number != 10:
        number = random.randint(1,10)
        if number == 10:
            break
        else:
            cycles += 1
            continue
    print(cycles)

def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    high = 10
    low = 0
    cycles_remaining = n

    if cycles_remaining != 0:
        number = random.randint(1,100)
        if number > high:
            high = number
            cycles_remaining -= 1
        elif number < low:
            low = number
            cycles_remaining -= 1
        else:
            cycles_remaining -= 1
    print(high + " " + low)
def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    reversed_string = ""
    for char in word:
        reversed_string = char + reversed_string
    return reversed_string

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("fizzbuzz")
        elif i % 3 == 0:
            results.append("fizz")
        elif i % 5 == 0:
            results.append("buzz")
        else:
            results.append(str(i))
    return " ".join(results)
def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """

    result_string = ""
    current_n = n

    while current_n != 1:
        result_string += str(current_n) + " "
        if current_n % 2 == 0:
            current_n //= 2  # Use integer division
        else:
            current_n = 3 * current_n + 1

    # Add the final '1' to the string
    result_string += str(current_n)

    return result_string


def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    if n <= 0:
        return ""
    elif n == 1:
        return "0"
    else:
        # Initialize list with first two Fibonacci numbers
        fib_sequence = [0, 1]

        # Generate subsequent numbers
        while len(fib_sequence) < n:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)

        # Convert list to a space-separated string
        fib_string = " ".join(map(str, fib_sequence[:n]))
        return fib_string


print(fibonacci(300))