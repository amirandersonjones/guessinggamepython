#importing the random call function of python
import random #import random

#make up some words to use for random words to guess
words = ['rainbow', 'fish', 'zebra','amazing', 'cobra','zoo','happy','money','inventing',
'surprise','shellfish','zodiac','pipefitter','gigantic','swimming','Sundays','ridiculous','love',
'special','absolutely','wreck','enormous','snake','superficial','dashing','radiance','extra','flight','computer','science','python','developer','basketball']

#call the random choice funtion of random import to pick a random word from the list
random_word=random.choice(words) #input the name of the list that we want the words to be selected from
#random_word =names the variable random_word to store the word that is chosen from the random list

print("our random word", random_word)# this line to test that the random call function actually works




print("The word is"), len(random_word), "letters long." # used to show how many letters are in the random word

output = ['_'] * len(random_word)

# function to print the output list
def print_output():
    print
    print(" ".join([x+" " for x in output]))

counter = 0
for i in range(1, 9):#gives the amount of guesses allocated
    print_output()
    letter = input("Guess a letter ")
    if letter in random_word:
        print("Correct"), letter #if guesses letter is correct print correct

        # now replace the underscores in the output-list with the correctly
        # guessed letters - on the same position the letter is in the 
        # secret word of course
        for i,x in enumerate(random_word):
            if x is letter:
                output[i] = letter
    counter +=1
    if counter == 8:
        print("You lost!")           
    else:
        print("Incorrect", " ", letter)
        #if its wrong print incorecct
    

    
