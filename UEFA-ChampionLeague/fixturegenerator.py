# UEFA Champion League Seeding for Knock-out Round
# by Huy Vu
"""
   UEFA Champion League is the most prestiged international
   football tournament for clubs in Europe which attracts
   hundred millions of audience worldwide

   Tournament Format:
   Upon qualification, 32 clubs around Europe are divided
   into 8 groups of 4 playing 2-leg round-robin. Winner
   and runner-up from each group advance to the knock-out phase.

   The first knock-out phase rule is complexly seeded according
   to the following UEFA rules:
   1/ Teams are group winners will not face each other
   2/ Teams are group runner-ups will not face each other
   3/ Teams from same group will not face each other
   4/ Teams from same country will not face each other
   5/ Groups winners play at home in the 2nd leg

   Ex: Team A - Team B
   meaning Team A plays at home in 1st leg
   and Team B plays at home in 2nd leg
   
   Later rounds will not be seeded, in which teams are randomly
   chosen at drawing.
   
   This module generate fixtures for the first knock-out
   round of the UEFA Champion League.
   
   Input file format:
   Winner Group A, Country
   Runnerup Group A, Country
   Winner Group B, Country
   Runnerup Group B, Country
   ...
   ...
   Winner Group H, Country
   Runnerup Group H, Country
"""

import sys,random

# read input
# read from command line
#f = open(str(sys.argv[1]),"r")
f = open("UCL11-12.txt","r")
lines = f.readlines()
f.close()

# strip off the \n character
for i in range(0,len(lines)):
        tmp = lines[i].strip().split(',')
        lines[i] = (tmp[0],tmp[1],chr(int(i/2)+65))
        
# split teams into group winners and runner-ups
groupwinners = lines[::2]
grouprunnerups = lines[1::2]


while len(grouprunnerups)>0:
        teamA = random.choice(grouprunnerups)
        grouprunnerups.remove(teamA)
        tempPot = []
        for tmp in groupwinners:
                if tmp[1] != teamA[1] and tmp[2] != teamA[2]:
                        tempPot.append(tmp)
        teamB = random.choice(tempPot)
        groupwinners.remove(teamB)
        print(teamA[0]+' - '+teamB[0])
        
                
        



