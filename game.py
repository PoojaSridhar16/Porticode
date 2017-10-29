import sys
import time
import pygame
import inputbox

print("Once upon a time, there was a guy called Hangman who was murdered. However, he came back as a ghost... People kept trying to kill him by hanging him, but when they couldn't, he came back to haunt them. Now, it's your turn to try. Beware, if you lose, he'll come back to haunt you for the rest of your life...\n")
print("First we need to see if you're smart enough to take on this challenge\n")
print("You will now have to answer some riddles, for each you get three tries. If you succeed, you get to take on hangman.\n")
    
questions = ["What runs around the whole yard without moving?",
             "There is a clerk at the butcher shop, he is five feet ten inches tall, and he wears size 13 sneakers. He has a wife and 2 kids. What does he weigh?",
             "I am a word of letters three, add two and fewer there will be. What am I?",
             "Sometimes I walk in front of you. Sometimes I walk behind you. It is only in the dark that I ever leave you. What am I?",
             "What has hands but can not clap?",
             "What begins with T, ends with T and has T in it?",
             "What has a head and a tail, but no body?",
             "What can travel around the world while staying in a corner?",
             "What kind of room has no doors or windows?"]

answers = ["fence",
           "meat",
           "few",
           "shadow",
           "clock",
           "teapot",
           "coin",
           "stamp",
           "mushroom"]

hints = ["It helps keep things in",
         "You can eat it",
         "Synonym for little",
         "It's caused by light",
         "It's an object",
         "Think of T as something to drink",
         "You can flip it",
         "You can lick it before you use it",
         "It's food"]


for x in range(0,9):
    print(questions[x], "\n")
    counter = 0
    message = input ("What is your answer? ").lower()
    while (counter <= 2):
        if (message == answers[x]):
            print("Correct!\n")
            break
        else:
            print("Try again")
            message = input ("What is your answer? ").lower()
        if(counter == 0 and message != answers[x]):
            print("Hint: ", hints[x])
        if(counter == 1 and message != answers[x]):
            print("You're not smart enough to take on the hangman.")
            sys.exit()
        counter += 1
        
pygame.init()

size = [950, 950]
screen=pygame.display.set_mode(size)

 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

state=0
print("Congratulations! You're good enough to go against Hangman. A new window has now opened for you, you can start guessing. You have 6 chances to save your life...")
word = "hangman"

remaining=word
guesses = ''
turns = 6

def show_hangman(screen, turns):
    screen.fill((0,0,0))
    screen.fill(WHITE)
        
    if (turns == 6):
        # do nothing
        print ("nothing to do")
        
    if (turns <= 5):
        #  show head
        pygame.draw.ellipse(screen, BLACK, [160, 100, 150, 120], 0)
        
    if (turns <= 4):
        pygame.draw.line(screen, BLACK, [240, 200], [240, 360], 12)
        
    if (turns <= 3):
        pygame.draw.line(screen, BLACK, [240, 240], [140, 300], 12)
        
    if (turns <= 2):
        pygame.draw.line(screen, BLACK, [240, 240], [340, 300], 12)
        
    if (turns <= 1):
        pygame.draw.line(screen, BLACK, [240, 360], [140, 460], 12)
        
    if (turns <= 0):
        pygame.draw.line(screen, BLACK, [240, 360], [340, 460], 12)
        
    pygame.display.update()
        
        

while True:
            
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()

    inp = str(inputbox.ask(screen, 'Message'))
    print ("Your guess " + inp)
        
    if inp == "quit":
        pygame.quit()
        sys.exit()
        
    if inp == "clear":
         screen.fill((0,0,0))
         
    show_hangman(screen, turns)
        
    print("Your status: ")
    displayWord = ""
    for char in word:
        if char in guesses:
            displayWord = displayWord + char
        else:
            displayWord = displayWord + "_"
            
    print (displayWord)
    displayWord = myfont.render(displayWord, True,  (200, 000, 000))
    screen.blit(displayWord, (20, 30))
    
    if turns>0:
        guess=inp
        
        if guess in remaining:
            
            remaining=remaining.replace(guess,'')
            print('Correct')
            guesses = guesses + guess
            
            # show the correct stuff on the screen
        else:
            
            # show an extra step
            turns-=1
            print('Wrong')        
            
        
        show_hangman(screen, turns)
        
        print("Your status: ")
        displayWord = ""
        for char in word:
            if char in guesses:
                displayWord = displayWord + char
            else:
                displayWord = displayWord + "_"
                
        print (displayWord)
        displayWord = myfont.render(displayWord, True,  (200, 000, 000))
        screen.blit(displayWord, (20, 30))
        
        if len(remaining)==0:
            screen.fill((0,0,0))
            screen.fill(WHITE)
            displayWord = "You won. Your life is safe, for now... Please type quit to return to your normal life."
            displayWord = myfont.render(displayWord, True,  (200, 000, 000))
            screen.blit(displayWord, (20, 80))
            
        print('You have', turns, 'more guesses')
    else:       
        screen.fill((0,0,0))
        screen.fill(WHITE)
        displayWord = "GAME OVER!! You cannot hide.The hangman is coming for you.Type quit and start running."
        displayWord = myfont.render(displayWord, True,  (200, 000, 000))
        screen.blit(displayWord, (20, 80))
        print('You lose')
            
    pygame.display.flip()
    pygame.display.update()
