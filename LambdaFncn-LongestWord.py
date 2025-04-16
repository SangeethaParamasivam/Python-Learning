'''*Lambda function assignment questions*
1. Write a lambda function that returns a function to calculate x^n, where n is given at runtime.
2. Write a lambda function to check if a given year is a leap year. (Hint: A year is a leap year if it is divisible by 4 and not by 100 unless also divisible by 400.)
3. Use a lambda function with reduce() to find the longest word in a list of strings.

3. Use a lambda function with reduce() to find the longest word in a list of strings'''
from functools import reduce

longest_word = lambda words: reduce(lambda a, b: a if len(a) >= len(b) else b, words)

words_list = ["apple", "banana", "cherry", "blueberry", "kiwi"]
print(longest_word(words_list))  
