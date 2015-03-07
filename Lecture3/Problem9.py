list = ('h','l','c')
epsilon = 1
low = 0
high = 100
result = (high+low)/2

print('Please think of a number between 0 and 100! ')

while abs(result**2 -result) >= epsilon or True:
    print ('Is your secret number '+str(result)+' ?')
    print ("Enter 'h' to indicate the guess is too high. "),
    print ("Enter 'l' to indicate the  guess is too low."),
    answer = raw_input ("Enter 'c' to indicate I guessed correctly.")
  
    if answer not in list:
        print('Sorry, I did not understand your input.')
    elif answer == 'c':
        break
    elif answer == 'h':
        high = result
    elif answer == 'l':
        low = result
    result = (high+low)/2
            
print('Game over. Your secret number was: ' +str(result))
