print ("="*120)
print (" "*45,"STUDENT MARKS CHECKER")
print ("="*120)

print ("NAME"," " *15,"MATHS"," " *10,"ENGLISH"," " *10,"URDU"," " *10,"TOTAL"," " *10,"PERCENTAGE"," " *12,"RESULT")
student_name_1 = "Abdul Kalam"
student_name_2 = "Muhammad Anees"
student_name_3 = "Mujeeb Khan"
student_name_4 = "Ahmad Hasan"

print ()

# subject_name1 = "Maths"
# subject_name2 = "English"
# subject_name3 = "Urdu"

maths_marks_student_1 = 97
english_marks_student_1 = 95
urdu_marks_student_1 = 87


total_marks_student_1 = 0
total_marks_student_1 += maths_marks_student_1
total_marks_student_1 += english_marks_student_1
total_marks_student_1 += urdu_marks_student_1

total_marks = 300
max_marks_subject = 100
passing_marks = 33
minimum_passing_marks = (passing_marks+passing_marks+passing_marks)
total_subjects = 3

percentage_student_1 = round((total_marks_student_1/total_marks)*100,2)

result_student_1 = minimum_passing_marks <= total_marks_student_1

print (student_name_1," " *9,maths_marks_student_1," " *14,english_marks_student_1," " *14,urdu_marks_student_1," " *12,total_marks_student_1," " *14,percentage_student_1," " *9,"First :",result_student_1)

maths_marks_student_2 = 69
english_marks_student_2 = 40
urdu_marks_student_2 = 54

total_marks_student_2 = 0
total_marks_student_2 += maths_marks_student_2
total_marks_student_2 += english_marks_student_2
total_marks_student_2 += urdu_marks_student_2

result_student_2 = minimum_passing_marks <= total_marks_student_2

percentage_student_2 = round((total_marks_student_2/total_marks)*100,2)
print (student_name_2," " *6,maths_marks_student_2," " *14,english_marks_student_2," " *14,urdu_marks_student_2," " *12,total_marks_student_2," " *14,percentage_student_2," "*7,"Second :",result_student_2)

maths_marks_student_3 = 28
english_marks_student_3 = 35
urdu_marks_student_3 = 30

total_marks_student_3 = 0
total_marks_student_3 += maths_marks_student_3
total_marks_student_3 += english_marks_student_3
total_marks_student_3 += urdu_marks_student_3

result_student_3 = total_marks_student_3 <= minimum_passing_marks

percentage_student_3 = round((total_marks_student_3/total_marks)*100,2)

print (student_name_3," " *9,maths_marks_student_3," " *14,english_marks_student_3," " *14,urdu_marks_student_3," " *12,total_marks_student_3," " *15,percentage_student_3," " *10,"Fail :",result_student_3)

maths_marks_student_4 = 92
english_marks_student_4 = 72
urdu_marks_student_4 = 97

total_marks_student_4 = 0
total_marks_student_4 += maths_marks_student_4
total_marks_student_4 += english_marks_student_4
total_marks_student_4 += urdu_marks_student_4

result_student_4 = total_marks_student_4 >= minimum_passing_marks

percentage_student_4 = round((total_marks_student_4/total_marks)*100,2)

print (student_name_4," " *9,maths_marks_student_4," " *14,english_marks_student_4," " *14,urdu_marks_student_4," " *12,total_marks_student_4," " *14,percentage_student_4," " *9,"First :",result_student_4)

print ("_" *120)

print (student_name_1,"passed :",(maths_marks_student_1 >= passing_marks and english_marks_student_1 >= passing_marks and urdu_marks_student_1 >= passing_marks)," First division....")
print (student_name_2,"passed :",(maths_marks_student_2 >= passing_marks and english_marks_student_2 >= passing_marks and urdu_marks_student_2 >= passing_marks)," Second division....")
print (student_name_3,"passed :", not (maths_marks_student_3 < passing_marks or english_marks_student_3 < passing_marks or urdu_marks_student_3 < passing_marks)," Try Next Year....")
print (student_name_4,"passed :",(maths_marks_student_4 >= passing_marks and english_marks_student_4 >= passing_marks and urdu_marks_student_4 >= passing_marks)," First division....") 
print ("=" *120)