#Grading system in school
#A:90-100
#B:80-90
#C:70-80
#D:60-70
#E:50-60

#multiple conditions

score= int(input("Enter the Score: \n"))

if score >=90 and score <=100:
    print("Grade is A")
elif score >=80 and score <=90:
    print("Grade is B")
elif score >=70 and score <=80:
    print("Grade is C")
elif score >=60 and score <=70:
    print("Grade is D")
elif score >=50 and score <=60:
    print("Grade is E")
else:
    print("Invalid Score")