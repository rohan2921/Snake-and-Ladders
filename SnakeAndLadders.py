# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:34:54 2019

@author: ROHAN
"""
from PIL import Image
import random as r
end=100
#showing the image of the board to the user
def show_board():
    img=Image.open('c:\\snake.png')
    img.show()


    
#starting the game by taking the players names as inpiut 
def play():
    p1Name = input('player 1 plesae enter your name')
    p2Name = input('player 2 name')
    #initialise points of user 1 and 2 to 0
    p1=0
    p2=0
    
    turn=0
    while(1):
        if turn%2==0:
            #player1 chance
            print(p1Name,' your turn ')
            print('Enetr 1 to play on 0 to continue : ')
            c=input()
            if(c=='0'):
                print(p1Name,' scored ',p1)
                print(p2Name,' scored ',p2)
                print('Thank you for playing....')
                break
            dice=int(r.randint(1,6)) #using rand int for getting dice number
            print('Dice showed ',dice)
            p1=p1+dice
            p1=checkLadder(p1)#calling the funtion to check if ladder encounterd
            p1=checkSnake(p1)#calling the funtion to check if snake encounterd
           # p1=int(p1)
            #end=int(end)
            if p1>end:
                p1=end
                
            print(p1Name,' score ',p1) 
            if reachedEnd(p1):
                print(p1Name,'won')              
        else:
              #player2 chance
              print(p2Name,' your turn ')
              print('Enetr 1 to play on 0 to continue : ')
              c=input()
              if(c=='0'):
                  print(p1Name,' scored ',p1)
                  print(p2Name,' scored ',p2)
                  print('Thank you for playing....')
                  break
              dice=int(r.randint(1,6)) #using rand int for getting dice number
              print('Dice showed ',dice)
              p2=p2+dice
              p2=checkLadder(p2)#calling the funtion to check if ladder encounterd
              p2=checkSnake(p2)#calling the funtion to check if snake encounterd
              #p2=int(p2)
              #end=int(end)
              if p2>end:
                  p2=end
              print(p2Name,' score ',p2)   
              if reachedEnd(p2):
                  print(p2Name,'won')   
                  
                  
                  
        turn=turn+1
             
def checkLadder(pos):
    if pos==5:
        print('Ladder')
        return 25
    elif pos==10:
        print('Ladder')
        return 29
    elif  pos==22:
        print('Ladder')
        return 41
    elif pos==28:
        print('Ladder')
        return 55
    elif pos==44:
        print('Ladder')
        return 95
    elif pos==70:
        print('Ladder')
        return 89
    elif pos==79:
        print('Ladder')
        return 81
    else:
        return pos


def checkSnake(pos):
    if pos==31:
        print('Snake')
        return 14
    elif pos==37:
        print('Snake')
        return 17
    elif pos==73:
        print('Snake')
        return 53
    elif pos==78:
        print('Snake')
        return 39
    elif pos==92:
        print('Snake')
        return 35
    elif pos==99:
        print('Snake')
        return 7
    else:
        return pos
            


def reachedEnd(pos):
    if pos==end:
        return True
    else:
        return False
              
              
              
         
     
         
    
show_board() 
 
play()