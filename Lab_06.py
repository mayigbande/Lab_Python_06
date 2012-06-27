# -*- coding: utf-8 -*-
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team
    def add_score(self,date,score):
       
        self.scores.append(score)
       
        
    def total_score(self):
        total=0
        for i in self.scores:
            total=total+i
        return total
        print total
        
    def average_score(self):
        average=0
        for i in self.scores:
            #total_score()
            average=float(self.total_score())/len(self.scores)
        print self.first_name+"' ","average score is:",average

      
import datetime

torres=[0,0,1,0,1]


    
Torres=Player('Torres','Fernado','Basa')
for i in range(len(torres)):
    Torres.add_score("2012/06/16",torres[i])
print Torres.scores
Torres.total_score()
Torres.average_score()
#Torres.add_score("2012/05/18",3)
#print Torres.scores

print "............................"
class Team:
    def __init__(self,name,league,manager_name,points):
        self.name=name
        self.league=league
        self.manager=manager_name
        self.points=points
        self.players=[]
    def add_player(self,player):
        self.players.append(player)
        #print self.players
    def __str__(self):
        return "the name of the team is"+' '+self.name
        
portugal=Team("portugal","la liga","mayi",30)
spain=Team("spain","la liga","calbert",34)
print spain
print portugal
torres= Player('Torres','Fernado',spain)
print torres.team.name
ronaldo=Player("Christiano","ronaldo",portugal)
print ronaldo.team.name
spain.add_player("torres")
portugal.add_player("ronaldo")
print spain.players
print portugal.players

class Match:
    def __init__(self,home_team,away_team,date):
        self.home_team=hometeam
        self.away_team=away_team
        self.date=date
        self.home_scores={}
        self.away_scores={}
    def home_score(self):
        self.home_scores[torres.team.name]=1
        print self.home_scores
    #def away_score(self):
        
#print spain.home_scores





        


#myPlayer.total_score()
#myPlayer.average_score()
