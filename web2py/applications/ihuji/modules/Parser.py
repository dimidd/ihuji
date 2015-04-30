__author__ = 'shaj'

# from
import re
import Regexes

class Parser:
    #Constant words
    EXAM_SYN = ["exam", "moed", "test"]
    TA_SYN = ["tirgul", "ta"]
    LECTURE_SYN = ["lecture", "shiur"]
    CLASS_SYN = ["class", "lesson"] + TA_SYN + LECTURE_SYN
    GRADE_SYN = ["grade", "score"]
    VOTE_SYN = ["vote"]

    NO_NAME_ERROR = "ERROR - COURSE NAME NOT SPECIFIED"

    def __init__(self):
        pass

    # Parses a string relative to the given student id
    def str_parser(self, str_to_parse, st_id):

        print "Hello, I'm a parser"         # delete
        print """You sent me: '""" + str_to_parse + """' and id: """ + str(st_id)         # delete

        #Search for one of the constant words
        # if matched with exam_syn -> parse_exam(str_to_parse, st_id)
        #else -> parse_class()

        str_to_parse = str.lower(str_to_parse).strip()

        print "the lower-cased str: " + str_to_parse        # delete

        exam_c = re.compile(Regexes.EXAM_MASSAGE)
        class_c = re.compile(Regexes.CLASS_MASSAGE)
        grade_c = re.compile(Regexes.GRADE_MASSAGE)
        vote_c = re.compile(Regexes.VOTE_MASSAGE)

        print "compiled things...."        # delete

        #print class_c.match(str_to_parse)

        #exam_c = re.compile("exam"|"moed"|"test")
        #class_c = re.compile("class"|"lecture"|"shiur"|"tirgul"|"ta")
        if vote_c.match(str_to_parse):
            print "vote matched...."        # delete
            self.parse_vote(str_to_parse, st_id)
        elif grade_c.match(str_to_parse):
            print "grade matched...."        # delete
            self.parse_grade(str_to_parse, st_id)
        elif exam_c.match(str_to_parse):
            print "exam matched...."        # delete
            self.parse_exam(str_to_parse, st_id)
        elif class_c.match(str_to_parse):
            print "class matched...."        # delete
            # try:
            #     self.parse_class(str_to_parse, st_id)
            # except Exception as e:
            #     print e.message;
            self.parse_class(str_to_parse, st_id)
        else:
            self.parse_unknown(str_to_parse, st_id)


        # tiles = [[0 for i in xrange(7)] for j in xrange(4)]
        # data = ""
        # inputfile = open(file_path)
        # for line in inputfile:
        #     data += line

        # data = re.sub(re.compile("/\*(.|[\r\n])*?\*/", re.DOTALL), "", data)
        # data = re.sub(re.compile("/\*\*(.|[\r\n])*?\*/", re.DOTALL), "", data)
        # data = re.sub(re.compile("\"\"\"(.|[\r\n])*?\"\"\"", re.DOTALL), "", data)
        # data = re.sub(re.compile("//.*"), "", data)
        # data = re.sub(re.compile("#.*"), "", data)
        #
        # data = data.replace(' ', '')
        # data = data.replace('\n', '')
        # data = data.replace('-', '')
        # data = data.replace(',', '')

        # r = 0
        # c = 0
        # for i in range(0, 83, 3):
        #     if r < int(num_of_players):
        #         tiles[r][int(data[i]) - 1] = Tile(int(data[i + 1]), int(data[i + 2]))
        #     else:
        #         tiles[r][c] = Tile(int(data[i + 1]), int(data[i + 2]))
        #     c += 1
        #     if c == 7:
        #         c = 0
        #         r += 1
        return "good"

    def parse_vote(self, str_to_parse, st_id):
        print "inside parse_vote() with id: " + str(st_id)  # delete
        str_to_parse = str_to_parse["vote".__len__():].strip()
        course_c = re.compile(Regexes.LESSON_ID)
        course_num = course_c.findall(str_to_parse)
        str_to_parse = str_to_parse[int(Regexes.LESSON_ID_LENGTH):].strip()
        print str_to_parse
        vote_c = re.compile(Regexes.VOTE_VALUE)
        vote = vote_c.findall(str_to_parse)

        self.mark_vote_at_course(vote, course_num)
        # # if exist c in course_names
        # course_c = re.compile('|'.join(course_names))
        # if course_c.match(str_to_parse):
        #     # return the course_name that appears
        #     pass
        # else:
        #     return ""
        #     pass


    def parse_grade(self, str_to_parse, st_id):
        print "inside parse_grade() with id: " + str(st_id)          # delete

        course_names = self.find_student_courses_names(st_id)
        # if exist c in course_names
        course_c = re.compile('|'.join(course_names))
        course_matched = "".join(course_c.findall(str_to_parse)[0])
        if course_matched:
            courseNum = self.find_course_num(course_matched)
            print "I'll go looking for your grade in course number " + str(courseNum)  # delete
            # return the course_name that appears
            pass
        else:
            return ""
            pass

    def parse_exam(self, str_to_parse, st_id):
        print "inside parse_exam() with id: " + str(st_id)           # delete

        course_names = self.find_student_courses_names(st_id)
        course_c = re.compile('|'.join(course_names))
        course_matched = "".join(course_c.findall(str_to_parse)[0])

        next_c = re.compile("next")
        #courseNum = None
        if course_matched:
            courseNum = self.find_course_num(course_matched)
            timeAndPlace = self.find_exam_time_place(courseNum)
            # return the course_name that appears
            pass
        elif next_c.match(str_to_parse):
            pass
            #TODO later, dealing with times
            #find_next_class(st_id)
            #datetime.time
        else:
            # No name was specified when looking for a grade
            raise Exception(self.NO_NAME_ERROR)
        pass


    def parse_class(self, str_to_parse, st_id):
        course_names = self.find_student_courses_names(st_id)
        course_c = re.compile('|'.join(course_names))
        course_matched = "".join(course_c.findall(str_to_parse)[0])

        next_c = re.compile("next")
        #courseNum = None
        if course_matched:
            courseNum = self.find_course_num(course_matched)
            timeAndPlace = self.find_class_time_place(str_to_parse, courseNum)
            # return the course_name that appears
            pass
        elif next_c.match(str_to_parse):
            pass
            #TODO later, dealing with times
            #find_next_class(st_id)
            #datetime.time
        else:
            # No name was specified when looking for a grade
            raise Exception(self.NO_NAME_ERROR)
        pass

    def parse_unknown(self, str_to_parse, st_id):
        print "YOU'VE SENT ME SOME UNKNOWN THINGS HERE..... CAN'T REALLY HELP YOU"

    # TODO implemets the search from the DB
    def find_student_courses_names(self, st_id):
        # returns a list with the name of all the courses the student with this id takes
        # searches the DB
        return ["infi", "linear algebra"]

    # TODO implemets the search from the DB
    def find_course_num(self, course_name):
        # searches the number of the course with the given name

        print "inside find_course_num with name: " + course_name             # delete

        if course_name == "infi":
            return 1
        elif course_name == "linear algebra":
            return 2
        else:
            return 0
        #pass

    # TODO implemets the search from the DB
    def find_exam_time_place(self, courseNum):
        # returns the time and place of the next exam in the course with the given number
        print "inside find_exam_time_place() with courseNum : " + str(courseNum)         # delete
        pass

    # TODO implemets the search from the DB
    def find_class_time_place(self, str_to_parse, courseNum):
        print "inside find_class_time_place() with courseNum : " + str(courseNum)        # delete
        print "the str to parse is: " + str_to_parse
        #--------------------------------------------------------------------------#
        ta_c = re.compile('|'.join(self.TA_SYN))
        lecture_c = re.compile('|'.join(self.LECTURE_SYN))
        if ta_c.match(str_to_parse):
            return self.find_TA_time_place(courseNum)
        #if lecture_c.match(str_to_parse):
            #return self.find_lecture_time_place(courseNum)
        # DEFAULT:
        return self.find_lecture_time_place(courseNum)
        # returns the time and place of the next class in the course with the given number
        pass

    # TODO implemets the search from the DB
    def find_TA_time_place(self, courseNum):
        print "inside find_TA_time_place() with courseNum : " + str(courseNum)       # delete
        # finds when this student's TA is of the given course num
        pass


    # TODO implemets the search from the DB
    def find_lecture_time_place(self, courseNum):
        print "inside find_lecture_time_place() with courseNum : " + str(courseNum)      # delete
        # finds when this student's LECTURE is of the given course num
        pass

    # TODO implemets something on the teacher's computer ha ha ha!!!
    def mark_vote_at_course(self, grade, course_num):
        print "inside mark_vote_at_course() with grade : " + str(grade) + " and course-num: " + str(course_num)     # delete
