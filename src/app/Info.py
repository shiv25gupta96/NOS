import json
import inspect
import os

Tournaments={}
Tournaments['Accounts']=[]
Tournaments['Accounts'].append({
    'User Name':'yo_yo_pubg',
    'Profile Name':'OFFICIAL PUBG TOURNAMETS',
    'link':'https://www.instagram.com/yo_yo_pubg/',
    #'Phone number':'',
    'unique id':'TRPG0001'

})
Tournaments['Accounts'].append({
    'User Name':'pubgtournaments2018',
    'Profile Name':'Regal Gaming',
    'Link': 'https://www.instagram.com/pubgtournaments2018/',
    #'phone number': '123456',
    'unique id': 'TRPG0002'
})
Tournaments['Accounts'].append({
    'User Name': 'pubg_tourment',
    'Profile Name': 'PUBG TOURNAMENT',
    'Link': 'https://www.instagram.com/pubg_tourment/',
    # 'phone number': '123456',
    'unique id': 'TRPG0003'
})
Tournaments['Accounts'].append({
    'User Name': 'pubg_champions_game',
    'Profile Name': 'PUBG TOURNAMENTS',
    'Link': 'https://www.instagram.com/pubg_champions_game/',
    # 'phone number': '123456',
    'unique id': 'TRPG0004'
})
Tournaments['Accounts'].append({
    'User Name': 'pubg_tournaments124',
    'Profile Name': 'PUBG TOURNAMENT',
    'Link': 'https://www.instagram.com/pubg_tournaments124/',
    # 'phone number': '123456',
    'unique id': 'TRPG0005'
})
Tournaments['Accounts'].append({
    'User Name': 'pubg_legend_tournament_',
    'Profile Name': 'pubg tournaments',
    'Link': 'https://www.instagram.com/pubg_legend_tournament_/',
    # 'phone number': '123456',
    'unique id': 'TRPG0006'
})
Tournaments['Accounts'].append({
    'User Name': 'pubg_.mobile._tournament_',
    'Profile Name': 'pubg battle',
    'Link': 'https://www.instagram.com/_pubg_.mobile._tournament_/',
    # 'phone number': '123456',
    'unique id': 'TRPG0007'
})
Tournaments['Accounts'].append({
    'User Name': 'pubg_tournaments_dailycash',
    'Profile Name': 'pubg tournaments',
    'Link': 'https://www.instagram.com/pubg_tournaments_dailycash/',
    # 'phone number': '123456',
    'unique id': 'TRPG0008'
})
Tournaments['Accounts'].append({
    'User Name': 'pubg.royal.tournaments',
    'Profile Name': 'PUBG TOURNAMENTS',
    'Link': 'https://www.instagram.com/pubg.royal.tournaments/',
    # 'phone number': '123456',
    'unique id': 'TRPG0009'
})
Tournaments['Accounts'].append({
    'User Name': 'pubgtournaments_daily',
    'Profile Name': 'Pubg Tournaments',
    'Link': 'https://www.instagram.com/pubgtournaments_daily/',
    # 'phone number': '123456',
    'unique id': 'TRPG0010'
})
print(Tournaments)
print(type(Tournaments))
with open(os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)+'\\data\\tournamentsData.ts','w') as outfile:
    json.dump(Tournaments,outfile)
