## start to match betting 

from fractions import Fraction

def utilities():
    def findOdds(odds):  ## useless as we can just put in float - may be useful if made into webscraper
        # find first odd
        firstOdd = [] 
        for i in range(len(odds)-1):
            if odds[i] == "/":
                break
            else:
                firstOdd.append(odds[i])
        # find second odd
        secondOdd = []
        for i in range(len(odds)-1):
            if odds[i] == "/":
                index = i + 1
        for i in range(index,len(odds)):
            secondOdd.append(odds[i])
        
        firstOdd = int(''.join(firstOdd))
        secondOdd = int(''.join(secondOdd))
        finalOdds = firstOdd/secondOdd

        return finalOdds  

        
    def checkReturns(r1,r2,r3,x1,x2,x3):
        total = x1 + x2 + x3
        if (r1 > total) and (r2 > total) and (r3 > total):
            return True
        elif (r1 == total) or (r2 == total) or (r3 == total):
            return "no prof for one outcome"
        else:
            return False

    def calculateReturns(stake,odds):
        return stake * (odds + 1)    
        
    ## calculate probability 
    def calculateProbability(odds):
        fractionOdds = Fraction(odds)
        denom = fractionOdds.denominator
        numer = fractionOdds.numerator
        return denom / (denom+numer)  ## doesnt give exact fraction gives a fraction cut at a certain decimal place e.g for 4/11 gives 3275345183542179/9007199254740992
            
    ## compare probabilities

    def compareProbabilies(p1,p2,p3):
        maxprob1 = max(p1,p2,p3)
        if maxprob1 == p1:
            return maxprob1, max(p2,p3)
        elif maxprob1 == p2:
            return maxprob1, max(p1,p3)
        else:
            return maxprob1, max(p1,p2)


    def matchedBetting(winOdds,drawOdds,lossOdds):
        pw = calculateProbability(winOdds)
        pd = calculateProbability(drawOdds)
        pl = calculateProbability(lossOdds)

        ## find way to relate the prob to the outcome - use a hashmap?
        ## fix the way that the fraction is not the same but a truncated value in calculate probabilities 

        ## the way its coded, compare probabilities will put the highest probability into first when outputting 

        p1,p2 = compareProbabilies(pw,pd,pl)


    ## this section could potentially be shortened using a hashmap

        if p1 == calculateProbability(winOdds):
            o1 = winOdds
        elif p1 == calculateProbability(drawOdds):
            o1 = drawOdds
        else:
            o1 = lossOdds

        if p2 == calculateProbability(winOdds):
            o2 = winOdds
        elif p2 == calculateProbability(drawOdds):
            o2 = drawOdds
        else:
            o2 = lossOdds

        maximisedArray = maximiseProfit(o1,o2)

        return 

    ## find the points to maximise profit for the other 2 probabilities - think of the graph
    def maximiseProfit(o1,o2):
        return




    ## find the points to maximise profit for the other 2 probabilities - think of the graph
    ## put all points into an array
    ## compare against the last probability to minimise loss
    ## check if works

    return

def twoWayBets(o1,o2,maxBet):

    # take the max bet and then compare and choose the best odds 

    # 3 possible eq to make the best odds:
    # x = a/(oi + 1)
    # x = a * oi/(oi + 1) => a - a/(oi + 1)
    # x = a/ (oi + 2)

    # make pairs for the different stakes - a set of pairs

    stakesSet = set()
    stakesSet.add((round((maxBet/(o1 + 1)),2) , round((maxBet - (maxBet/(o1 + 1))),2)))
    stakesSet.add((round((maxBet - (maxBet/(o1 + 1))),2) , round((maxBet/(o1 + 1)),2)))
    
    stakesSet.add((round((maxBet* (o1/(o1 + 1))),2) , round((maxBet - (maxBet* (o1/(o1 + 1)))),2)))
    stakesSet.add((round((maxBet - (maxBet* (o1/(o1 + 1)))),2) , round((maxBet* (o1/(o1 + 1))),2)))   # check if there is a reverse function for pairs 
    
    stakesSet.add((round((maxBet/(o1 + 2)),2) , round((maxBet - (maxBet/(o1 + 2))),2)))
    stakesSet.add((round((maxBet - (maxBet/(o1 + 2))),2) , round((maxBet/(o1 + 2)),2)))

    stakesSet.add((round((maxBet/(o2 + 1)),2) , round((maxBet - (maxBet/(o2 + 1))),2)))
    stakesSet.add((round((maxBet - (maxBet/(o2 + 1))),2) , round((maxBet/(o2 + 1)),2)))
    
    stakesSet.add((round((maxBet* (o2/(o2 + 1))),2) , round((maxBet - (maxBet* (o2/(o2 + 1)))),2)))
    stakesSet.add((round((maxBet - (maxBet* (o2/(o2 + 1)))),2) , round((maxBet* (o2/(o2 + 1))),2)))   # check if there is a reverse function for pairs  
    
    stakesSet.add((round((maxBet/(o2 + 2)),2) , round((maxBet - (maxBet/(o2 + 2))),2)))
    stakesSet.add((round((maxBet - (maxBet/(o2 + 2))),2) , round((maxBet/(o2 + 2)),2)))

    # some duplicates still come through - need to adjust that
    # made a set with all possible stakes in form of (o1,o2)

    # put it into a hashset or hashmap

    outcomelist = {}

    for i in stakesSet:
        outcome1 = round((i[0]* (o1 + 1)),2)
        outcome2 = round((i[1]* (o2 + 1)),2)

        # this gets rid of a totally losing bet 
        if outcome1 < maxBet and outcome2 < maxBet:          # need to make this more general and not just maxbet
            continue
        # this gets rid of any bets where the loss is greater than profit 
        elif outcome1 + outcome2 - 80 < 0:                    
            continue
        elif outcome1 >= maxBet and outcome2 >= maxBet:
            outcomelist[str(i)] = (round(outcome1 -maxBet,2), round(outcome2 - maxBet),2)
            #outcomelist[i] = (outcome1,outcome2)

        # else:
        #     outcomelist[i] = (outcome1,outcome2)

    return outcomelist

def convert_odds(odds):
    try:
        # Check if the odds are in fractional format like "6/4"
        if '/' in odds:
            num, denom = odds.split('/')
            return float(num) / float(denom)
        else:
            return float(odds)
    except ValueError:
        return None       


        

print(twoWayBets(11/8,8/15,40))
#print(twoWayBets(6/4,9/5,20,40))
#print(twoWayBets(6/5,8/11,20,40))






#print(matchedBetting(6/5,2/1,14/5))