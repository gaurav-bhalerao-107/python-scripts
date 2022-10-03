def mascara(d):
    if 0 <= d < 10:
        return str(d)
    elif d == 10:
        return "A"
    elif d == 11:
        return "B"
    elif d == 12:
        return "C"
    elif d == 13:
        return "D"
    elif d == 14:
        return "E"
    elif d == 15:
        return "F"
    else:
        return None


def converte(dec, b):
    if dec < b:
        return mascara(dec)
    else:
        return converte(dec // b, b) + mascara(dec % b)


# Converte decimal integers greater than zero to base from 2 to the base 16
num_decimal_lido = int(input("Enter the number: "))
while num_decimal_lido > 0 and num_decimal_lido != 0:
    print("Convertions results:")
    for base in range(2, 17):
        print("Base", str(base) + ":", converte(num_decimal_lido, base))
    print()
    num_decimal_lido = int(input("Enter with another number (0 to quit): "))