#!/usr/bin/env python3

#import statements 
import time
import os

#main function
def main():
    print("Let's see how well you are doing in school.")
    #wait a few seconds
    time.sleep(3)
    print("For today we only care about your math score.")
    time.sleep(2)
    os.system("clear")
    
    #Prompt user for a grade
    score = int(input("What is your Math grade?"))
    
    #if-else logic
    if score >= 90 :
        print("You have an 'A'")
    elif score >= 80:
        print("You have a 'B'")
    elif score >= 70:
        print("you have a 'C'")
    elif score <= 69:
        print("Please pack your things. Failures aren't allowed here.")
    else:
        print("Please input numerals to represent your score")
main()
