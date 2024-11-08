def squared(num) : return num*num

print (squared (2))


addtwo = lambda num: num+2
print (addtwo(12))

########################################

def funcbuilder(x):
    return lambda num: num + x

addten= funcbuilder(10)
addtwenty= funcbuilder(20)

print (addten(7))
print (addtwenty(7))


###########################
# odd numbers filter

numbers=[2,3,7,9,11,21,22,24,28]

odd_numbers= filter(lambda num: num%2 !=0, numbers)
print(list(odd_numbers))

#################################
