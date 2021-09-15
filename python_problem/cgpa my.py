

classes=[]
grades=[]


def collect():
    i=0
    while (i<=5):
        
        courseTitle=input("Enter your course title : ")
        classes.append(courseTitle)
        
        i+=1

    print(classes)

    y=0

    while ( y <= 5 ):
        grade=input("enter your grade for each class listed in order(int form): ")
        grade=grade.upper()
        grades.append(grade)
        
        
        y+=1

    calculator()
    
def calculator():
    total=0
    for element in grades:
        if element ==80:
            total=total+80
        elif element==75:
            total=total+75
        elif element==70:
            total=tatal+70
        elif element==65:
            total=tatal+65
        elif element==60:
            total=tatal+60
        elif element==55:
            total=tatal+55
        elif element==50:
            total=tatal+50
        elif element==45:
            total=total+45
        elif element ==40:
            total=total+40

    gpa=total/ 6
    print (gpa)
    

collect()
        
        
