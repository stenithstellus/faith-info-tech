#2 assignment fabinocci series
n=int(input('enter the number of terms:'))
a=0
b=1
if n<=0:
    print('the output of your input is',a)
else:
    print(a,b,end=' ')
    for x in range(2,n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c




 #PALIN DROME ARE NOT



# Converting the input number n to a sequence (string).

n=str(input('enter name:'))
# Checking whether the reversed sequence and the original sequence are equal or not.
if (n == "".join(reversed(n))):
    print("Palindrome")
else:
    print("Not a Palindrome")

# #assignment 1 rotate string
def rotate(L,n):
    if n==0:
        return
    if n>0:
        for i in range(n):
            x=L.pop()
            L.insert(0,x)
    else:
        for i in range(-n):
            x=L.pop(0)
            L.append(x)
L=[1,2,3,4,5,6,7,8,9]
n=int(input('enter the integer'))
rotate(L,n)
print(L)

#calculate the number of digits and letters in an string
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      elif(i.isalpha()):
            count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)

# assignment 1
# number guessing game
import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
