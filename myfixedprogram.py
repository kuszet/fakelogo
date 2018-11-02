#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:56:21 2018

@author: kuba
"""

import turtle
def wprawo():
        angle = float(input('Enter your next line angle: '))
        linelen = float(input('Enter your next line length: '))
        colour = input('Enter your next line colour: ')
        turtle.color(colour)
        turtle.right(angle)
        turtle.forward(linelen)
        if linelen and angle and colour != 0:
            angle = int(input('Enter your next line angle: '))
            linelen = int(input('Enter your next line length: '))
            colour = input('Enter your next line colour: ')
            turtle.color(colour)
            turtle.right(angle)
            turtle.forward(linelen)
def wlewo():
        angle = float(input('Enter your next line angle: '))
        linelen = float(input('Enter your next line length: '))
        colour = input('Enter your next line colour: ')
        turtle.color(colour)
        turtle.left(angle)
        turtle.forward(linelen)
        if linelen and angle and colour != 0:
            angle = float(input('Enter your next line angle: '))
            linelen = float(input('Enter your next line length: '))
            colour = input('Enter your next line colour: ')
            turtle.color(colour)
            turtle.left(angle)
            turtle.forward(linelen)
def figurki(numofang, linelen):
    for dupsko in range(numofang):
        turtle.forward(linelen)
        turtle.right(360/numofang)
                    
                     
                                         
declar = input('Welcome to the "fakeLogo", do you wanna play? y/n: ')
y = True
while y:
    if declar == 'n':
        print('')
        print('Nie to nie kurwa.')
    if declar == 'y':
        decision = input('Do you want to make straight lines or maybe some figure? lines/figure: ')
        if decision == 'figure':
            linelen = int(input('Enter your line length: '))
            numofang = int(input('Enter number of angles: '))
            figurki.figurki(numofang, linelen)
        else:
            print('')
            print('Good for you!')
            direction = input('In which direction you want your line to move? left/right: ')
            if direction == 'left':
                wlewo()
            elif direction == 'right':
                wprawo()
            more = input('Do you want to make another line? y/n: ')
            if more == 'y':
                pass
            else:
                y = False
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    