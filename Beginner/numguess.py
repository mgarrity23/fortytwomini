import random

play = True
while(play):
    range = int(input('Set a number greater than 20: '))
    num = random.randint(1, range)
    count = 0
    while True:
        guess = int(input('Guess the number: '))
        if guess == num:
            count += 1
            print('You got it right!')
            print('It took you ' + str(count) + ' guesses')
            break
        elif guess != num and count == 0:
            count += 1
            mod10 = num % 10
            print('Not quite. (hint the number mod 10 is ' + str(mod10) + ')')
        elif guess != num and count == 1:
            count += 1
            div10 = num // 10
            print('Not quite. (hint the number div 10 is ' + str(div10) + ')')
        elif guess > num and count > 1:
            count += 1
            print('The number is less than ' + str(guess))
        else:
            count += 1
            print('The number is greater than ' + str(guess))
    endres = input('Enter yes to play again: ')
    endlow = endres.lower()
    if endlow != 'yes':
        play = False
