'''*Arrays assignment questions*
1. Remove all duplicates from a list without using set()
2. Count the number of even and odd numbers in a list

1. Remove all duplicates from a list without using set()'''

my_list = [1, 2, 3, 4, 5, 5]

my_list = list(dict.fromkeys(my_list))


print(my_list)
