"""The purpose of this activity is to get your team, as a team, to think through a computational problem
and come up with an interesting computational solution. There are multiple possible ways to solve this
problem.
In professional golf tournaments, a tournament typically lasts four rounds. A player’s score is the sum of
the scores in the rounds (the lower the better). It is common for all players to play the first two rounds
of golf. However, only a fraction of the players are allowed to continue on to the third and fourth
rounds. The way this is done is that a “cut” score is determined, and those whose scores are better (i.e.
lower) than the cut are allowed to play the remainder of the tournament (they “made the cut”) while
the rest do not.
In this case, the cut will be the median score among the golfers. You are to print out the names of
golfers who made the cut (whose score was below the median), and those who did not make the cut
(score above the median). Thus, about half the golfers should make the cut. Here are some details:
• You are to write a program that reads in golfers’ names, and their first and second round scores.
Specifically, they should enter the first round score on one line, then the second round score on
another line, then the player’s name on a third line. This should continue for an arbitrary
number of players. The user should indicate that they are done entering players by giving a 
negative score for the first round – at this point, the reading-in of data should stop (without
reading a second round or player name).
• In practice, a common way to find the median is typically to sort the numbers from smallest to
largest, and then to find the median from there directly (either the middle element if an odd
number of elements., or the average of the two middle elements if an even number of
elements). There is a simple sort routine built in to Python, but you are not to use it (the builtin sort command) for this problem.
• There are many ways to find a median. A major part of this problem is to figure out a method
for finding the median, yourselves. There are solutions involving just multiple loops, there are
solutions that will use more than one list, and so on. Also, you do not technically have to find a
median – you could just find a way to report both those above and those below the median.
• You’ll be outputting two sets of names. Be sure it is clear which is which.
• Do this project as a team. The idea is that you should talk through the problem and develop a
solution together. Be sure to use good code development, as discussed before."""
k = 0
names = []
first = []
second = []
score = []
round1 =1
above = []
below = []
while round1 >= 0:
    round1 = int(input('Score for round 1: '))
    if round1 < 0:
        break
    else:
        round2 = int(input('Score for round 2: '))
        name = input('Name: ')
        first.append(round1)
        second.append(round2)
        names.append(name)

for k in range(len(names)):
    score.append(int(first[k]) + int(second[k]))

keydict = dict(zip(names, score))
names.sort(key=keydict.get)


for k in range(len(names)):
    if k >= (len(names) / 2):
        above.append(names[k])
    elif k < (len(names) / 2):
        below.append(names[k])

print('people who made the cut:', below)
print('people who did not make the cut:',above)
