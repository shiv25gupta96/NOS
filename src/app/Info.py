import json
import inspect
import os
import sys

with open(os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)+'\\data\\global.txt', 'r') as in_gb:
    g_uni_page_id = in_gb.read().strip()

class Tournament:
    tournament = {}
    def __init__(self, tournament):
        self.tournament = tournament

    def __str__(self):
        print(self.tournament)

quit = int(sys.argv[1])

tournaments=[]

while quit != 1:
    name = input("Name: ")
    link = input("Tournament Link: ")
    quit = input("Yes/No: ")
    tour = Tournament({ "p_name": name, "p_link": link  })
    tournaments.append(tour)

for tournament in tournaments:
    print(tournament.tournament)


with open(os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)+'\\data\\tournamentsData.ts','r') as outfile:
    file_content = outfile.read().strip()
    file_content = file_content[file_content.find("Accounts") + len("Accounts ="):].strip()
    tournaments = json.loads(file_content)
    
print tournaments[0]
    
