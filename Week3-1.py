from random import randint
if __name__ == '__main__':
  print('Numbers from 1 to 10')
  number = randint(1,10)
  while True:
    guess = int(input('Guess the number: '))
    if guess == number:
      print('Great! You did it!')
      break
