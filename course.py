class Course:
    courseID= "CS2401"
    teacher = "Dan DeBlasio"
    RMPRating = 5.0
    Start = 11001
    End = 01352
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