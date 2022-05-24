'''
FIZZ-BUZZ MULTIPLICATION TABLE
Create a function called fizz_buzz_table that takes a positive integer (n) as an input, and returns the
n x n multiplication table in a two dimensional array, where the “fizz-buzz” numbers are represented by
 their “fizz-buzz” string. A number is a “fizz-buzz” number if it’s a multiple of 3 or 5. If it’s a
  multiple of 3, it’s value should be Fizz. If it’s a multiple of 5, it’s value should be Buzz. If it’s
  a multiple of both 3 and 5, it’s value should be FizzBuzz.

  1 2 3
  2 4 6
  3 6 9
'''

def fizz_buzz_table(n):
    def fizz_buzz(product):
        if product % 3 == 0 and product % 5 == 0:
            return "fizzbuzz"
        elif product % 3 == 0:
            return "fizz"
        elif product % 5 == 0:
            return "buzz"
        else:
            return product

    if not type(n) is int or n < 0:
        raise TypeError("Only positive integers are allowed")
    else:
        table = []
        for row in range(1,n+1):
            nums = [fizz_buzz(row * col) for col in range(1,n+1)]
            table.append(nums)
        print(table)



fizz_buzz_table(3)
fizz_buzz_table(5)

'''
Most common word
Write a function that can read and parse a file. It should take the name of the file as an input and
return the most common word of the file (case insensitively). If multiple words are found as the most 
common you can decide which one to return. You can assume that:
the file contains multiple lines
the words are separated by spaces only
there can be , and . characters in the sentences
The function should handle possible exceptions by printing messages to the standard output.'''

def find_most_common(filename):
    if not type(filename) is str:
        print("Input filename as string, for example 'sample.txt'")
    else:
        try:
            text = ""
            with open(filename, "r") as list_obj:
                for line in list_obj.readlines():
                    text += line.lower().replace(".","").replace(",","")
                word_count = {word : text.split().count(word) for word in text.split()}
                most_common_word = max(word_count, key=word_count.get)
            print(most_common_word)
        except FileNotFoundError:
            print("File not found, input valid filename, for example 'sample.txt'")


