print('How many cats do you have?')
number_cats = input()
try:
    if int(number_cats) < 0:
        print('The number must be bigger than 0.')
    elif int(number_cats) >= 4:
        print('That is a lot of cats!')
    else:
        print('That is not that many cats!')
except ValueError:
    print('You did not enter a number.')
