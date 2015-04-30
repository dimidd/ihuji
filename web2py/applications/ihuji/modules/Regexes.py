__author__ = 'shaj'

import re
LESSON_ID_LENGTH = '5'

# Regex

#Voting Regexes
#----------------
VOTE = '(^vote\s)'
LESSON_ID = '(\s*\d{'+ LESSON_ID_LENGTH +'}\s)'
COMMENTS = '(\w+)'
VOTE_VALUE = '(\s*[1-5]\s*)'

VOTE_MASSAGE = '(' + VOTE + LESSON_ID + VOTE_VALUE + ')' + '|' + '('+ VOTE + LESSON_ID + COMMENTS + ')'

#Exam Regexes
#--------------
EXAM = '(\s(exam|moed|test))'
COURSE_NAME = '(^(\w+\s*)+)'

EXAM_MASSAGE = '(' + COURSE_NAME + EXAM + ')'


#Class Regexes
#--------------
CLASS = '(\s(class|tirgul|ta|lecture|shiur|lesson))'

CLASS_MASSAGE = '(' + COURSE_NAME + CLASS + ')'


#Grade Regexes
#--------------
GRADE = '(\s(grade|score))'

GRADE_MASSAGE = '(' + COURSE_NAME + GRADE + ')'
