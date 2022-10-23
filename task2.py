def generateLists(list):
    dividedBy2 = []
    dividedBy3 = []
    dividedBy5 = []
    for i in list:
        if(i % 2 == 0):
            dividedBy2.append(i)
        if(i % 3 == 0):
            dividedBy3.append(i)
        if(i % 5 == 0):
            dividedBy5.append(i)
    return (dividedBy2, dividedBy3, dividedBy5)