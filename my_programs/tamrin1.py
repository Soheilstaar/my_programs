hads = input('enter your number of choice: ')
sum=0
count = 0
while int(hads) != -1:
    print('hadse shoma', hads)
    sum = sum + int(hads)
    count = count + 1
    print('tedade hads ta alan', count,'va majmoo ta alan', sum)
    hads = input('enter your number of choice: ')
print('The AVERAGE is   ' , sum/count)