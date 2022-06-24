#The Perfect Guess Game
import random
def updateCountInFile(count_of_guesses):
    count=0
    with open('score.txt','r') as f:
        count=f.read() #count will be in string format 
    if(count_of_guesses < int(count)): 
        print("Congratulations, you have set a new record.")
        with open('score.txt','w')as f: #updating the file with lower score
            f.write(str(count_of_guesses)) #write() does not take int parameter so typecasting it to str
     
def isTheGuessCorrect(usr_guess,compNum):
    if(usr_guess == compNum):
        print("****** Hurray..!!! It's a correct guess. ******")
        return 'y'
    elif(usr_guess > compNum):
        print("Lower number please")
        return 'n'
    elif(usr_guess < compNum):
        print("Higher number please")
        return 'n'
    

def guessGame():
    count_of_guesses = 0 #initially zero
    comp_rand_Number = random.randint(1,10)
    while(True):
        user_guess = int(input('Guess the number(1-10) : '))
        if(user_guess > 10 or user_guess < 1):
            print("Please select a Number from 1-10 only")
            guessGame()
        else:
            any_one_won=isTheGuessCorrect(user_guess,comp_rand_Number)
            count_of_guesses+=1
            if(any_one_won=='y'):
                break
    #once someone wins condition will break
    print("Number of Guesses made: ",count_of_guesses)


    updateCountInFile(count_of_guesses)
    


print('--------- The Perfect Guess ---------')
guessGame()