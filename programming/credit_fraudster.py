
def checkLuhn(purportedCC=''):
    sum_ = 0
    parity = len(purportedCC) % 2
    for i, digit in enumerate([int(x) for x in purportedCC]):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum_ += digit
    return sum_ % 10 == 0
    
# 123457 * 43999900000 = 5432095654300000 < 543210******1234
# 123457 * 44000090000 = 5432119111130000 > 543210******1234
if __name__ == '__main__':
    min = 43999900000
    max = 44000090000
    for i in range(min, max):
        result = str(i * 123457)
        if ((result[0:5] == '54321') and (result[12:16] == '1234')): 
            #print(result)
            if (checkLuhn(result)):
                print(result)
