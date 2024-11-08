name = ('Soheil')
count = 1

def scope():
    print(name)
    global count
    count +=1
    print(count)

scope()