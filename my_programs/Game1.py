import random
javab = random.randint(1,10)

hads = input('Hads Bezan')
hads = int(hads)


while hads != javab:
    if hads < javab :
        print ('Kame')
    else:
        print ('ziade')
    hads = input('Hads Bezan')
    hads = int(hads)

print ('Afarin !', 'Javab', javab, 'bood !','va hadse shoma', hads,'bood :)')
