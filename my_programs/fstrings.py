person='Soheil'
coins=4

#1
print ('\n'+person+' has '+str(coins)+' coins left.')

#2
message=('\n%s has %s Coins left.') %(person,coins)
print (message)

#3
message2= ('\n{} has {} coins left.').format(person,coins)
print (message2)

#4
message3= ('\n{0} has {1} coins left.').format(person,coins)
print (message3)

#5
message4= ('\n{person} has {coins} coins left.').format(person=person,coins=coins)
print (message4)

#6 : Dictionary method
player = {'person':'Soheil', 'coins' : 4}
message5= ('\n{person} has {coins} coins left.').format(**player)
print (message5)

#7 : f-strings method
message6= (f'\n{person} has {coins} coins left.')
print (message6)
