acronyms = {'LOL': 'Laugh out Loud',
            'IDK': "I don'nt Know",
            'TBH': 'To Be Honet'}
acronyms['TBH'] = 'To be Honest Cool'  # if key exists it replaces
del acronyms['TBH']  # del the key from dictionary
definition = acronyms.get('BTW')
if definition:
    print(definition)
else:
    print("key does'nt exists")

print(acronyms)
