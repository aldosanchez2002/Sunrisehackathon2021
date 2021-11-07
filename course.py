class Course:
    courseID= "CS2401"
    teacher = "Dan DeBlasio"
    RMPRating = 1.01
    Start = 2355
    End = 2400
    Days = ['M', 'T']
    ADAAccess = False;
    lecture = '0'
    CRN = 25554

    # parameterized constructor
    def __init__(self):
        self.courseID = self.courseID
        self.teacher = self.teacher
        self.RMPRating = self.RMPRating
        self.Start = self.Start
        self.End = self.End
        self.Days = self.Days
        self.ADAAccess = self.ADAAccess
        self.lecture = self.lecture
        self.CRN = self.CRN



    def setAll(self,courseID, teacher, RMPRating, Start, End, Days, ADAAccess, lecture, CRN):
        self.teacher = teacher
        self.courseID=courseID
        self.RMPRating = RMPRating
        self.Start = Start
        self.End = End
        self.Days = Days
        self.ADAAccess = ADAAccess
        self.lecture = lecture
        self.CRN = CRN

    def setCourseId(self,courseID):
        self.courseID=courseID
    def setTeacher(self,teacher):
        self.teacher=teacher
    def setRMPating(self,RMPRating):
        self.RMPRating=RMPRating
    def setStart(self,Start):
        self.Start=Start
    def setEnd(self,End):
        self.End=End
    def setADAAcess(self,ADAAccess):
        self.ADAAccess=ADAAccess
    def setDays(self,Days):
        self.Days = Days
    def setLecture(self,lecture):
        self.lecture=lecture
    def setCRN(self,CRN):
        self.CRN=CRN

    def getCourseId(self):
        return self.courseID
    def getTeacher(self):
        return self.teacher
    def getRMPRating(self):
        return self.RMPRating
    def getStart(self):
        return self.Start
    def getEnd(self):
        return self.End
    def getADAAcess(self):
        return self.ADAAccess
    def getDays(self):
        return self.Days
    def getLecture(self):
        return self.lecture
    def getCRN(self):
        return self.CRN

    def display(self):
        print(" Course: " + str(self.courseID))
        print(" Teacher " + str(self.teacher))
        print(" CRN: " + str(self.CRN))
        print

    def displaySolution(self):
        print(" Course: " + str(self.courseID)+"   CRN: " + str(self.CRN))

def makeGM():

    c1 = Course()
    c1.setAll("CS2302","Diego Aguirre",5,20130,20250,['M','W'],True,"In-Person",21736)
    c1.display()
    c2 = Course()
    c2.setAll("CS2302","Olac Fuentes",3.4,21200,20120,['T','R'],True,"In-Person",25686)
    c2.display()
    c3 = Course()
    c3.setAll("CS2302"	,	"Olac Fuentes"	,	3.4	,	1330	,	1450	,	['T','R']	,	True	,	"In-Person"	,	27090)
    c3.display()
    cs = [c1,c2,c3]
    c4 = Course()
    c4.setAll("MATH3323"	,	"Luis Valdez-Sanchez"	,	2	,	1330	,	1450	,	['T','R']	,	True	,	"In-Person"	,	22534)
    c4.display()
    c5 = Course()
    c5.setAll("MATH3323"	,	"Luis Valdez-Sanchez"	,	2	,	1030	,	1150	,	['M','W']	,	True	,	"In-Person"	,	21021)
    c5.display()
    c6 = Course()
    c6.setAll("MATH3323"	,	"Miguel Argaez"	,	2.9	,	1030	,	1150	,	['T','R']	,	True	,	"In-Person"	,	21022)
    c6.display()
    c7 = Course()
    c7.setAll("MATH3323"	,	"Juio Cesar Urenda"	,	3.3	,	900	,	1020	,	['M','W']	,	False	,	"In-Person"	,	21178)
    c7.display()
    c8 = Course()
    c8.setAll("MATH3323"	,	"Juio Cesar Urenda"	,	3.3	,	-1	,	-1	,	[]	,	True	,	"ONLINE"	,	22449)
    c8.display()
    c9 = Course()
    c9.setAll("MATH3323"	,	"Juio Cesar Urenda"	,	3.3	,	-1	,	-1	,	[]	,	True	,	"ONLINE"	,	22739)
    c9.display()
    c10 = Course()
    c10.setAll("MATH3323"	,	"Juio Cesar Urenda"	,	3.3	,	-1	,	-1	,	[]	,	True	,	"ONLINE"	,	25661)
    c10.display()
    math=[c4,c5,c6,c7,c8,c9,c10]
    c11 = Course()
    c11.setAll("EE2169"	,	"TBA"	,	-1	,	730	,	1020	,	['R']	,	True	,	"ONLINE"	,	28762)
    c11.display()
    c12 = Course()
    c12.setAll("EE2169"	,	"TBA"	,	-1	,	1030	,	0120	,	['T']	,	True	,	"ONLINE"	,	25554)
    c12.display()
    c13 = Course()
    ee1=[c11,c12]
    c13.setAll("EE2369"	,	"Virgilio Ernesto Gonzalez"	,	-1	,	1330	,	1450	,	['M','W']	,	True	,	"In-Person"	,	23278)
    c13.display()
    c14= Course()
    c14.setAll("EE2369"	,	"Tahsin Rahman"	,	5	,	1500	,	1620	,	['T','R']	,	True	,	"In-Person"	,	25137)
    c14.display()
    ee2=[c13,c14]

    GM=[cs,math,ee1,ee2]
    print
    print("////////////////////////////")
    print("////////////////////////////")
    print("////////////////////////////")
    print
    return GM

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

def getValids(GM):
    valids=[]
    for a in range(0,len(GM[0])):
        for b in range(0, len(GM[1])):
            for c in range(0, len(GM[2])):
                for d in range(0, len(GM[3])):
                    if isValid([GM[0][a],GM[1][b],GM[2][c],GM[3][d]]):
                        valids.append([GM[0][a],GM[1][b],GM[2][c],GM[3][d]])
    return valids

def getBest(valids):
    tempMax=[Course(),Course()]
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
if __name__ == '__main__':
    getFinal()
