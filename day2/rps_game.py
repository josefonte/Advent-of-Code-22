from enum import Enum

class play(Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"

def readInput(filepath):
    with open(filepath, 'r') as file:
            lines = file.readlines()

    plays = []

    for line in lines:
        args = line.replace('\n', ' ').split(' ')
        pair = (args[0],args[1])
        plays.append(pair)

    return plays

def translatePlays(plays : list):
    c=0
    for p in plays:
        bot, me = p
        
        if bot == "A" : bot = play.ROCK  
        elif bot == "B" : bot = play.PAPER 
        elif bot == "C" : bot = play.SCISSORS 

        if me == "X" : me = play.ROCK  
        elif me == "Y" : me = play.PAPER 
        elif me == "Z" : me = play.SCISSORS 
        
        plays[c]= (bot,me)
        c +=1


    return plays

def translatePlaysResults(plays : list):
    c=0
    for p in plays:
        bot, result = p
        #print("bot: " + str(bot) + " | me: "+ str(me))
        
        if bot == "A" : 
            bot = play.ROCK  
            if result == "X": me = play.SCISSORS
            elif result == "Y": me = play.ROCK
            elif result == "Z": me = play.PAPER

        elif bot == "B" : 
            bot = play.PAPER 
            if result == "X": me = play.ROCK
            elif result == "Y": me = play.PAPER
            elif result == "Z": me = play.SCISSORS

        elif bot == "C" : 
            bot = play.SCISSORS 
            if result == "X": me = play.PAPER
            elif result == "Y": me = play.SCISSORS
            elif result == "Z": me = play.ROCK
        
        
        plays[c]= (bot,me)
        c +=1


    return plays


def calcPont(bot, me):
    pont =0
    if bot == play.ROCK : 
        if me ==  play.ROCK : pont = 1 + 3
        elif me ==  play.PAPER : pont = 2 + 6
        elif me ==  play.SCISSORS : pont = 3 + 0

    if bot == play.PAPER : 
        if me ==  play.ROCK : pont = 1 + 0
        elif me ==  play.PAPER : pont = 2 + 3
        elif me ==  play.SCISSORS : pont = 3 + 6
    
    if bot == play.SCISSORS : 
        if me ==  play.ROCK : pont = 1 + 6
        elif me ==  play.PAPER : pont = 2 + 0
        elif me ==  play.SCISSORS : pont = 3 + 3

    return pont


def main():
    plays = readInput("input.txt")  
    plays = translatePlaysResults(plays)

    ponts = []

    for p in plays:
        bot, me  = p
        pont = calcPont(bot,me)
        ponts.append(pont)

        print ("BOT : " + str(bot) + " | ME : " + str(me) + " | PONT : " + str(pont))

    print(sum(ponts))


if __name__ == "__main__" :
    main()