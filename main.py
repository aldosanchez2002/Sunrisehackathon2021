from course import Course
import bestRated
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
    return GM

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bestRated.getFinal()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
