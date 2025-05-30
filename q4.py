def check_number(string_number, number1_digit, number2_digit):
    sum = int(string_number[0:number1_digit]) + int(string_number[number1_digit:number1_digit+number2_digit])
    new_string = string_number
    sum_digit = max(number2_digit, number1_digit)
    if sum == int(string_number[(number1_digit+number2_digit):(number1_digit+number2_digit+sum_digit)]):
        if len(string_number) == number1_digit + number2_digit + sum_digit:
            return ("", 0, 0)
        new_string = string_number[number1_digit:]
    if sum == int(string_number[(number1_digit+number2_digit):(number1_digit+number2_digit+sum_digit+1)]):
        if len(string_number) == number1_digit + number2_digit + sum_digit + 1:
            return ("", 0, 0)
        new_string = string_number[number1_digit:]
        sum_digit += 1
    return (new_string, number2_digit, sum_digit)


number=input()
if len(number) < 3:
    print("NO")
    exit()
    
if int(number[0]) + int(number[1]) == int(number[2]) or int(number[0]) + int(number[1]) == int(number[2:4]):
    digit1 = 1
    digit2 = 1  
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()

        
if len(number) > 3 and (int(number[0]) + int(number[1:3]) == int(number[3:5]) or int(number[0]) + int(number[1:3]) == int(number[3:6])):
    digit1 = 1
    digit2 = 2
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()
        
if len(number) > 4 and (int(number[0]) + int(number[1:4]) == int(number[4:7]) or int(number[0]) + int(number[1:4]) == int(number[4:8])):
    digit1 = 1
    digit2 = 3
    flag = 0
    num = number
    while num != "":

        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()

if len(number) > 3 and (int(number[0:2]) + int(number[2]) == int(number[3:5]) or   int(number[0:2]) + int(number[2]) == int(number[3:6])):
    digit1 = 2
    digit2 = 1
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()

if len(number) > 4 and (int(number[0:2]) + int(number[2:4]) == int(number[4:6]) or   int(number[0:2]) + int(number[2:4]) == int(number[4:7])):
    digit1 = 2
    digit2 = 2
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()
        
if len(number) > 5 and (int(number[0:2]) + int(number[2:5]) == int(number[5:8]) or   int(number[0:2]) + int(number[2:5]) == int(number[5:9])):
    digit1 = 2
    digit2 = 3
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()
        
if len(number) > 4 and (int(number[0:3]) + int(number[3]) == int(number[4:7]) or   int(number[0:3]) + int(number[3]) == int(number[4:8])):
    digit1 = 3
    digit2 = 1
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()        

if len(number) > 5 and (int(number[0:3]) + int(number[3:5]) == int(number[5:8]) or   int(number[0:3]) + int(number[3:5]) == int(number[5:9])):
    digit1 = 3
    digit2 = 2
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()

if len(number) > 6 and (int(number[0:3]) + int(number[3:6]) == int(number[6:9]) or   int(number[0:3]) + int(number[3:6]) == int(number[6:10])):
    digit1 = 3
    digit2 = 3
    flag = 0
    num = number
    while num != "":
        (new_number, digit1, digit2) = check_number(num, digit1, digit2)
        if num == new_number:
            flag = 1
            break
        num = new_number
    if flag == 0:
        print("YES")
        exit()
        
print("NO")