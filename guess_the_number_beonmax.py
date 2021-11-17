import random

class Game:

    @staticmethod
    def guess_the_number():

        attempt = 6
        c = 1

        while c <= attempt:
            n = int(input('Enter any number between 1 and 50 : '))
            rand_num = random.randint(1,50)

            if n > rand_num:
                print('The number you enter is greater than the random number ! Try again. ')

            elif n < rand_num:
                print('The number you enter is less than the random number ! Try again. ')

            elif n == rand_num:
                print('The number is guessed. Congradulations !')
                break

            elif n != rand_num and attempt == 6:
                print(f'You didn\'t guess the number. My number was {rand_num}')
                break

            c += 1

object = Game()

object.guess_the_number()
