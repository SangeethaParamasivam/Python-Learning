''' 
Grade Calculator using 

*Objective*:
Create a program that takes a numeric grade as input and returns the corresponding letter grade
using Python's match-case statement.

*Requirements*:
1. Create a function called 'calculate_grade' that takes a numeric score as input
2. Use match-case statements to determine the letter grade
3. Return the appropriate letter grade based on the following scale:
   - 90-100: 'A'
   - 80-89: 'B'
   - 70-79: 'C'
   - 60-69: 'D'
   - Below 60: 'F'
4. Include input validation to handle non-numeric inputs and scores outside the valid range (0-100)

*Example Usage*:
>>> calculate_grade(95)
'A'
>>> calculate_grade(82)
'B'
>>> calculate_grade(45)
'F'
'''


calculate_grade = int(input("Enter your numerical grade from 0 to 100: ")) 

match calculate_grade:
    case grade if 90 <= grade <= 100:
        print("Grade: A")
    case grade if 80 <= grade < 90:
        print("Grade: B")
    case grade if 70 <= grade < 80:
        print("Grade: C")
    case grade if 60 <= grade < 70:
        print("Grade: D")
    case grade if 0 <= grade < 60:
        print("Grade: F")
    case _:
        print("Enter numerical grade from 0 to 100 only!")
