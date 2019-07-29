import random
import matplotlib.pyplot as plt
import numpy as np

money = 10000
betamount = 100
plays = 100
tests = 100

#returns true if player wins
def diceroll():
    roll = random.randint(1,100)
    outcome = lambda roll: True if roll > 51 else False
    return outcome(roll)

#creates a zip object with diceroll,fundsleft for all plays
def bet(totalfunds, wager, totalplays):
    fundsleft = [totalfunds]
    plays = [-1]
    for i in range(totalplays):
        plays.append(i)
        if diceroll() == True:
            fundsleft.append(fundsleft[i]+wager)
        else:
            fundsleft.append(fundsleft[i]-wager)
    return zip(plays,fundsleft)

#creates a list of zip objects for numoftimes trials
def trials(numoftimes):
    x = 0
    alltrials = []
    while x <= numoftimes-1:
        alltrials.append(bet(money,betamount,plays))
        x = x+1
    return alltrials

def averagewinnings(lst):
    temp = sum(lst)/len(lst)
    return temp

def percentwin(lst):
    count = 0
    for i in lst:
        if i >= money:
            count = count+1
        else: continue
    return (count/len(lst))*100

arraytrials = np.array(list(trials(tests)))
arraytrialsy = np.array(list(trials(tests)))

#plots the individual plays for each trial
outcome = []
for i in range(tests):
    xvals = [a for (a,b) in arraytrials[i]]
    yvals = [b for (a,b) in arraytrialsy[i]]
    outcome.append(yvals[-1])
    plt.scatter(xvals,yvals)
    plt.plot(xvals,yvals,linewidth=0.5)

#average winning and percent chance
print('Average Winnings in '+str(tests)+' trials: $',averagewinnings(outcome))
print(percentwin(outcome),'% chance to win')
print(float(100)-percentwin(outcome),'% chance to lose')

#show the graph with axis labels
plt.xlabel('Number of Plays')
plt.ylabel('Funds Left')
plt.show()