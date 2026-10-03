#PART 1

def is_valid_part(part):
    """Error Checking"""
    if not isinstance(part, int):   #if part isnt an integer
        print("Not a number.")
        return False
    elif isinstance(part, int):     #if part is an integer
        #Was gonna do a leading zeroes check, but pycharm does it for me apparently lol
        if part > 255 or part < 0:  #if part is more than 255 or less than 0
            return False
        elif part > 0 and part < 255:   #If part is more than 0 and less than 255
            return True


def is_valid_ip(ip):
    #ip should be a string!
    partlist = ip.split('.')    #ip is split into 4 parts
    if len(partlist) == 4:      #if partlist has 4 items in the list
        if int(partlist[0]) == 0:   #if first part of list equals the integer 0
            return False
        else:
            for parts in partlist:      #repeat below for each item in the list
                is_valid_part(int(parts))   #turns parts into an integer for is_valid_part to understand
                if is_valid_part == False:  #if the results of is_valid_part is false
                    return False
                else:
                    return True
    elif len(partlist) != 4:    #if partlist doesnt have 4 items in the list
        return False            #frick off lmao

print(is_valid_ip("255.1.1.10"))

#PART 2
result = ''

def decimal_to_binary(n):
    if n == 0:
        return '0'
    elif n >= 1:
        decimal_to_binary(n // 2)    #runs decimal_to_binary for the result of n / 2 round down
        global result           #pulls in the result var outside the function
        result += str(n % 2)       #result equals the remainder of n % 2 turned into a string?
        return result


print(decimal_to_binary(255))

#i feel like i cheated with this one, but honest to god i had no other ideas

def binary_to_decimal(b):
    if b == " ":
        return 0
    else:
        d = int(b, 2)
        return d

print(binary_to_decimal('101010'))

#just to test something...

def d_to_b2(n):
    if n == '0':
        return '0'
    elif n >= '1':
        b = int(n, 10)
        return b

print(d_to_b2("255"))

#okay that didnt work