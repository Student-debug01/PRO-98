def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


   // Hint 2

	with open(file2, 'r') as b:
    data_b = b.read()

   // Hint 3

    with open(file2, 'w') as b:
    b.write(data_a)

swapFileData()
