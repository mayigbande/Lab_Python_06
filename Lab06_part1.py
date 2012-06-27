"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""
import datetime
## create the player_stats data structure
player_stats={datetime.date(2012,06,23):['rooney',2],
              datetime.date(2012,06,25):['rooney',2],
              datetime.date(2012,06,19):['ronaldo',0],
              datetime.date(2012,06,20):['ronaldo',3],
              datetime.date(2012,06,21):['torres',1]}
#print player_stats['rooney']



## implement highest_score
def highest_score(num):
    list=[]
    highest=0
    date=0
    for i in player_stats.keys():
        plays=player_stats[i]
        if plays[1]>highest:
            highest=plays[1]
            date=i
            name=plays[0]
    print "(",name,",",date,",",highest,")"
highest_score(player_stats)

## implement highest_score_for_player
def highest_score_for_player(player_stat,player):
    highest=0
 
    for i in player_stats.keys():
        plays=player_stats[i]
        if plays[0]==player:
            if(plays[1]>highest):
                highest=plays[1]
    print "the highest number of goals for",inputs,"is",highest
    
    
inputs=raw_input("enter a name:")
highest_score_for_player(player_stats,inputs)
                
                
## implement highest_scorer

def highest_scorer(player_stats):
    sum1=0
    sum2=0
    sum3=0
    highestsum=0
    name=""
    for i in player_stats:
        scores=player_stats[i]
        if scores[0]=='ronaldo':
            sum1=sum1+scores[1]
            highestsum=sum1
            name=scores[0]
        if scores[0]=='rooney':
            sum2=sum2+scores[1]
            if(sum2>sum1):
                highestsum=sum2
                name=scores[0]
        if scores[0]=='torres':
            sum3=sum3+scores[1]
            if sum3>sum1 or sum3>sum2:
                highestsum=sum3
                name-scores[0]
            
    print name,"has the highest number of",highestsum,"goals"
highest_scorer(player_stats)
    
'''
highest=0
    list=[]
    name=""
    for j in player_stats.keys():
        scores=player_stats[j]
        if scores[0]==inputs:
            highest=highest+scores[1]
            name=scores[0]
            #return name,highest
    print name,highest
inputs=raw_input("enter a name")
highest_scorer(player_stats)
'''  
