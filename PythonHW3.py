
import random
words=["computer","mouse","software","keyboard","apple","game","programming","mind"]
name=input("Please enter your name: ")
print("Welcome {}".format(name.capitalize()))
count=10
guess=0
word = random.choice(words)
print("Word length is: ",len(word))
print("Guess the characters")
guesses =''
while count > 0:
    # counts the number of user fails
    fail = 0
    for c in words: 
        if c in guesses: 
            print(c)
        else: 
            fail += 1
    guess = input("guess a character:")
    guesses+=guess 
    if guess in word: 
            print("True")
            print("your guesses : {}".format(guesses))
            if word==guess:
                print("CONGRATULATIONS!\n The word is {}".format(word))
                print("OYUN BİTTİ")
                break
    else:
           count-= 1
           print("Wrong")
           print("your guesses : {}".format(guesses))
           print("You have", + count, 'more guesses')
           if count == 0:
                print("You Loose! Word is {}".format(word))
                print("The word is: ",word) 