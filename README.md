# Magazine
Laba1
p = 1
while p != 0:
print "Select a section:"
    print "1. sale of goods"
    print "2. delivery of goods"
    print "3. sales data"
    #product_name = ''
    first_number = input('enter the number: ')
    my_file = open('sklad.txt', 'r')
    my_string = my_file.read()
    if (first_number == 1):
        print(my_string)
        my_file.close()
        while True:
            print "That you want to enter?"
            print "1. id"
            print "2. name"
            second_number = input('enter the number: ')
            if (second_number == 1):
                id = input('enter id goods: ')
                quantity = input('enter the number of units: ')
                J = input('generate purchase? ')
            elif (second_number == 2):
                name = input('enter the product name: ')
                quantity = input('enter the number of units: ')
                J = input('generate purchase? ')
            else:
                J = 0
            if (J == 0):
                break
    if (first_number == 2):
        id = input('enter id goods: ')
        delivery_number = input('enter the number of units shipped: ')
        if (id > 5):
            product_name = input('enter product name: ')
            price = input('enter price: ')
            #my_file = open("sklad.txt", 'a')
            """content = ['{} {} {} {}'.format(s.split()[1],
                              s.split()[2], s.split()[3],
                              s.split()[4]) for s in my_file.read().split('\n')]
            content.append('{} {}'.format(id, product_name, price, delivery_number))
            my_file.write("id, product_name, price, delivery_number")"""
            my_file = open('sklad.txt', 'r')
            my_string = my_file.read()
            print(my_string)
            my_file.close()
    if (first_number == 3):
        my_file = open("prodaja.txt", "w")
        my_file.write("")
        my_file = open("prodaja.txt", "r")
        my_string = my_file.read()
        print(my_string)
        my_file.close()  
    p = input('All? ')
