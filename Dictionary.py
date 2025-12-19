capitals ={'USA':'Washington DC',
            'India':'New Delhi', 
            'China':'Beijing', 
            'Russia':'Moscow'}

print(capitals['Russia'])
print(capitals.get('India'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())


capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'New York'})
capitals.pop('China')
capitals.clear()

for key,value in capitals.items():
    print(key,value)