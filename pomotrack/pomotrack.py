import time
import pickle
import random
from interval import Interval




def start_interval(interval_length):
    input("Start? > ")
    mins = interval_length
    while mins != 0:
        print(">>>>> {}".format(mins))
        print_motivation()
        time.sleep(60)
        mins = mins - 1
            
    rating = int(input("Please rate your interval.On a Scale 0 to 10 \n"))
    interval = Interval(rating,interval_length)
    return interval
        

def start_pause(pause_length):
        mins = pause_length
        while mins != 0:
            print(">>>>> {}".format(mins))
            time.sleep(60)
            mins -= 1

def print_motivation():
    motivation = ["Keep on","you're getting there","I believe in you","For Sparta","Do it, JUST DO IT","you got it champ","work hard", "work harder", "stop slacking", "wwjd"]
    print(random.choice(motivation))

def main():
    filewriter = open('log.obj','w')
    print("Hi, are you ready to get stuff done?\n")
    interval_length = int(input("Then put in your interval length and confirm with enter. \n"))
    pause_length = int(input("Now enter your pause length. \n"))
    while(True):
        pickle.dump(start_interval(interval_length),open("log.p","wb"))
        start_pause(pause_length)
        continue_work = input("Continue? Enter (Y)es or (N)o)\n")
        if (continue_work == 'n') or (continue_work == 'N'):
            print("goodbye")
            break



if __name__ == "__main__":
    main()

