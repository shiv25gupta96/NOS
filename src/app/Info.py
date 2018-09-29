import json

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
print(Tournaments)
print(type(Tournaments))
with open('Tournaments.txt','w') as outfile:
    json.dump(Tournaments,outfile)
