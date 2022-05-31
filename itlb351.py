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
    STRING_FOR_DIVISIBLE_BY_3 = "Fizz"
    STRING_FOR_DIVISIBLE_BY_5 = "Buzz"

    def fizz_buzz(product):
        fizz_buzzed_product = ""
        if product % 3 == 0:
            fizz_buzzed_product += STRING_FOR_DIVISIBLE_BY_3
        if product % 5 == 0:
            fizz_buzzed_product += STRING_FOR_DIVISIBLE_BY_5
        if fizz_buzzed_product == "":
            fizz_buzzed_product = str(product)
        return fizz_buzzed_product


    if not isinstance(n, int):
        raise TypeError("Only positive integers are allowed")
    if n < 0:
        raise ValueError("Integer should be positive")      #raise will stop the code if error, dont need else statement

    table = []
    for row in range(n):
        numbers = [fizz_buzz((row + 1) * (column + 1)) for column in range(n)]
        table.append(numbers)
    return print(table)



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
    def clean_text(text, separators=[".",","]):
        for separator in separators:
            text = text.replace(separator,"")
        return text.lower().split()

    def get_word_count(file):
        word_count = {}
        for line in file:
            cleaned_text_list = clean_text(line)
            for word in cleaned_text_list:
                word_count[word] = word_count.get(word,0) + 1
        return word_count

    if not isinstance(filename,str):
        raise TypeError("Input filename as string, for example 'sample.txt'")
    with open(filename, "r") as file:
        word_count = get_word_count(file)
        most_common_word = max(word_count, key=word_count.get)
    return most_common_word
# no need for FileNotFoundError and ValueError (empty file) handling because there is built-in exception

print(find_most_common("sample.txt"))
