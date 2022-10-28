from random import randrange

random_number = randrange(1000)
while True:
    try:
        value = int(input('type a number: '))
        if random_number == value:
            print('you win')
            break
        print('smaller' if (random_number<value) else 'bigger')

    except ValueError:
        print('this is not a number')
        continue