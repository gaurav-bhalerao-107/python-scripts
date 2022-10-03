from math import trunc

numbers = list(map(str, range(10)))
numbers += ["A", "B", "C", "D", "E", "F"]
list_numbers_hex = list(enumerate(numbers))


def from_int_to_hex(int_number):
    """
    Convert an integer number to hexadecimal
    use recursion
    """
    if int_number < 16:
        return list(filter(lambda e: e[0] == int_number, list_numbers_hex))[0][1]
    while int_number >= 16:
        return from_int_to_hex(trunc(int_number / 16)) + from_int_to_hex(
            int_number % 16
        )


def aux_validate_int(txt_int_number):
    """
    Validate an int number
    """
    txt_int_number = txt_int_number.strip().upper()
    if str(txt_int_number).isdigit():
        return int(txt_int_number)
    return False


if __name__ == "__main__":
    print("-" * 50)
    while not (int_number := aux_validate_int(input("Informe an integer number: "))):
        print("NUMBERS only! [0-9]")
    print(f"{int_number}(int) to hex is: {from_int_to_hex(int_number)}")
    print("-" * 50)
