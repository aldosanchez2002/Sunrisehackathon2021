from main import makeGM
def getValids(GM):
    valids=[]
    for a in range(0,len(GM[0])):
        for b in range(0, len(GM[1])):
            for c in range(0, len(GM[2])):
                for d in range(0, len(GM[3])):
                    if isValid([GM[0][a],GM[1][b],GM[2][c],GM[3][d]]):
                        valids.append([GM[0][a],GM[1][b],GM[2][c],GM[3][d]])
    return valids

def isValid(arrOfCourses):
    gms=[]
    temp = arrOfCourses[0]
    temp.display()
    while len(arrOfCourses)>0:
        for x in range(0,len(arrOfCourses)-1):
            if arrOfCourses[x].getStart() < temp.getStart():
                temp=arrOfCourses[x]
        gms.append(arrOfCourses[x])
        temp = arrOfCourses[0]
        arrOfCourses.remove(temp)

    for x in range(len(gms)-2):
        if gms[x].getEnd()>=gms[x+1].getStart():
            return False
    return True

def getBest(valids):
    tempMax=valids[0]
    for c in valids:
        if sumRating(c)>sumRating(tempMax):
            tempMax = c
    return tempMax

def sumRating(c):
    sum =0
    for a in c:
        sum = sum + a.getRMPRating()
    return sum

def getFinal():
    valids=getValids(makeGM())
    bestChoice =getBest(valids)
    print("RESULT")
    for c in bestChoice:
        c.displaySolution()
    return bestChoice