my_list = [0, 1, 2, 3, 4]
an_equal_list = list(range(5))

for my_number in range(10):
    print(my_number)

list(range(10))

[my_number * 2 for my_number in range(10)]

1 % 2
0
5 % 2
8 % 3

[n for n in range(10) if n % 2 == 0]

names_list = ["John", "Rolf", "Anne"]
lowercase_names = [name.lower() for name in names_list]
print(lowercase_names)
