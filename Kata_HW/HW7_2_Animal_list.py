def list_animals(animals):
    list = ''
    x=0
    for i in  range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
        x+=1
    return list