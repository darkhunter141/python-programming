class Result_sheet:
	def __init__(self):
		print("please enter your marks")
	
	def Grade_point(self,marks):
		marks = int(marks)
		if marks>=80 and marks<=100:
			return "A+"
		elif marks>=70:
			return "A"
		elif marks>=60:
			return "A-"
		elif marks>=50:
			return "B"
		elif marks>=40:
			return "C"
		elif marks>=33:
			return "D"
		else:
			return "F"	
grade_point_table = {
		'A+':4.0,
	'A':3.75,
	'A-':3.5,
	'B':3.0,
	'C':2.0,
	'D':1.0,
	'F':0
	}
obj = Result_sheet()
subject = ("Bangla","English", "Math", "Islamic_studies","Social_science","ICT","Physics","Chemistry","Biology","Higher_Math")
total_grade_point = 0
result_with_details = [["SUBJECT", "MARK", "GRADE","GRADE_POINT"]]
for i in range(len(subject)):
	print("enter your marks for "+subject[i])
	mark = int(input())
	
	if mark > 100:
		print('please insert valid mark')
		print("enter your marks for "+subject[i])
		mark = int(input())
		continue
		
	
	grade = obj.Grade_point(mark)
	total_grade_point += grade_point_table[grade]
	result_with_details.append([subject[i],mark,grade,grade_point_table[grade]])
print("\n\n")

name = str(input("enter your name: "))

roll = int(input("enter your roll number: "))
print("\n\n")

print("Welcome to your Result_Sheet")
print("Name : ",name)
print("Roll_Number : ", roll)
print("\n\n")
for i in result_with_details:
	print(*i, sep='      \t')
print("\n")
print("your total grade point is : %.2f" % total_grade_point)
print("\n")
CGPA = total_grade_point/10
print("your CGPA is = %.2f" % CGPA)