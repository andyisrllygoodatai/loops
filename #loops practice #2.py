#loops practice #2
list1 = range(1,1001)
for number in list1:
    if number % 2 == 0:
        print(f'mumber is even {number}')
    else:
        print("This number is not even")
#sum
print(f'the sum of the list is {sum(list1)}')                