p = 'Нет'
R = 'Нет'
k = 0
flag = 0
while p != 'Да':
    print ("Выберите раздел:")
    print ("1. Продажа товара")
    print ("2. Поставка товара")
    print ("3. Данные по продажам")
    first_number = int(input('Введите число: '))
    my_file = open('склад.txt', 'r+')
    my_string = my_file.readlines()
    my_sale = open('продажи.txt', 'r+')
    my_str = my_sale.readlines()
    if (first_number == 1):
        for i in my_string:
            print(i)
        my_file.close()
        while R !='Да':
            print ("Чего вы хотите ввести?")
            print ("1. id")
            print ("2. название")
            second_number = int(input('Введите число: '))
            if (second_number == 1):
                ident = int(input('Введите id товара: '))
                quantity = int(input('Введите количество единиц товара: '))
                for i in my_string:
                    i = i.split(',')
                    if ident == int(i[0]) and quantity <= int(i[3]) and quantity >= 0:
                        my_string[k] = my_string[k].split(',')
                        i[3] = str(int(i[3]) - quantity) + '\n'
                        my_string[k] = i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3]
                        my_str += str(i[0]) + ',' + str(int(i[2])*quantity) + ' руб' + '\n'
                        with open('склад.txt', 'w') as my_file:
                            for i in my_string:
                                my_file.writelines(i)
                        my_file.close()
                        with open ('продажи.txt', 'w') as my_sale:
                            for j in my_str:
                                my_sale.writelines(j)
                        my_sale.close()    
                        R = input('Сформировать покупку? ')
                        if R == 'Да':
                            print('Спасибо за покупку!\n')
                        break
                    k += 1
                k = 0
                
            elif (second_number == 2):
                name = input('Введите название продукта: ')
                quantity = int(input('Введите количество единиц товара: '))
                for i in my_string:
                    i = i.split(',')
                    if name == i[1] and quantity <= int(i[3]) and quantity >= 0:
                        my_string[k] = my_string[k].split(',')
                        i[3] = str(int(i[3]) - quantity) + '\n'
                        my_string[k] = i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3]
                        my_str += str(i[0]) + ',' + str(int(i[2])*quantity) + ' руб' + '\n'
                        with open('склад.txt', 'w') as my_file:
                            for i in my_string:
                                my_file.writelines(i)
                        my_file.close()
                        with open ('продажи.txt', 'w') as my_sale:
                            for j in my_str:
                                my_sale.writelines(j)
                        my_sale.close()    
                        R = input('Сформировать покупку? ')
                        if R == 'Да':
                            print('Спасибо за покупку!\n')
                        break
                    k += 1
                k = 0
            else:
                R = input('Сформировать покупку? ')
                if R == 'Да':
                    print('Спасибо за покупку!\n')
                    break
    if first_number == 2:
        my_file = open('склад.txt', 'r+')
        my_string = my_file.readlines()
        for i in my_string:
            print(i)
        my_file.close()
        ident = int(input('Введите id товара: '))
        delivery_number = int(input('Введите количество поставляемых единиц товара: '))
        for i in my_string:
            i = i.split(',')
            if ident == int(i[0]):
                flag += 1
                i[3] = str(int(i[3]) + delivery_number)
                my_string[k] = i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3] + '\n'
                with open('склад.txt', 'w') as my_file:
                    for i in my_string:
                        my_file.writelines(i)
                my_file.close()
            k += 1
        if flag == 0:
            name = input('Введите название товара: ')
            price = int(input('Введите цену: '))
            with open('склад.txt', 'w') as my_file:
                my_string += str(ident) + ',' + str(name) + ',' + str(price) + ',' + str(delivery_number) + '\n'
                for i in my_string:
                    my_file.writelines(i)
            my_file.close()
        flag = 0    
        k = 0    
    if (first_number == 3):
        my_sale = open("продажи.txt", "r+")
        my_str = my_sale.read()
        print(my_str)
        my_sale.close()
    R = 'Нет'    
    p = input('Все? ')
