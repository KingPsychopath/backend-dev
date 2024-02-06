# Student Records

A school principal contacted me, seeking a program to securely store student information and automatically calculate letter grades based on scores. The program will simplify grading and course management for teachers, allowing them to focus on individual student needs. The program must maintain student privacy for enrolled courses.
Challenge

Complete the Student class.
Constructor

The constructor should take the following parameters (in order) and set them to the corresponding instance variables:

    name = name
    scores = scores

It should also initialize a private data member called __courses to an empty dictionary.
calculate_letter_grade method

It should take a score as a parameter.

    If score is 90 or above the function should return "A"
    If score is between 80 and 89 (inclusive) the function should return "B"
    If score is between 70 and 79 (inclusive) the function should return "C"
    If score is between 60 and 69 (inclusive) the function should return "D"
    Otherwise, the function should return "F"

add_course method

It should take a course_name and score as parameters.

    It should calculate_letter_grade based on the score.
    It should set the course_name as a key in the courses dictionary and the calculated letter grade as the corresponding value.

get_courses method

It should return the private __courses dictionary.

