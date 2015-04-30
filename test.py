
__author__ = 'shaj'
import re
from Parser import Parser
import Regexes
from datetime import date
from datetime import time

def main():

    print "TESTING THE STR1"

    STR = "vote 89324 this lesson sucks"

    vote_c = re.compile(Regexes.VOTE)
    voteCommand = vote_c.findall(STR)
    print voteCommand
    STR = STR[voteCommand.pop().__len__():]

    lesson_id_c = re.compile(Regexes.LESSON_ID)
    lessonIdCommand = lesson_id_c.findall(STR)
    print lessonIdCommand
    STR = STR[lessonIdCommand.pop().__len__():]

    vote_val_c = re.compile(Regexes.VOTE_VALUE)
    voteValCommand = vote_val_c.findall(STR)
    if voteValCommand:
        print voteValCommand
        STR = STR[voteValCommand.pop().__len__():]

    comment_c = re.compile(Regexes.COMMENTS)
    commentCommand = comment_c.findall(STR)
    print commentCommand

    #-----------------------------------------------------------#

    print "\nTESTING THE STR2"
    STR2 = "vote 89324 3 this lesson sucks"

    vote_c = re.compile(Regexes.VOTE)
    voteCommand = vote_c.findall(STR2)
    print voteCommand
    STR2 = STR2[voteCommand.pop().__len__():]

    lesson_id_c = re.compile(Regexes.LESSON_ID)
    lessonIdCommand = lesson_id_c.findall(STR2)
    print lessonIdCommand
    STR2 = STR2[lessonIdCommand.pop().__len__():]

    vote_val_c = re.compile(Regexes.VOTE_VALUE)
    voteValCommand = vote_val_c.findall(STR2)
    if voteValCommand:
        print voteValCommand
        STR2 = STR2[voteValCommand.pop().__len__():]

    comment_c = re.compile(Regexes.COMMENTS)
    commentCommand = comment_c.findall(STR2)
    print commentCommand

    #------------------------------------------------------------

    # TESTING THE ENTIRE STRING
    print "\nTESTING THE ENTIRE STRING"
    STR = "vote 89324 3 this lesson sucks"

    vote_message_c = re.compile(Regexes.VOTE_MASSAGE)
    voteMassageCommand = vote_message_c.findall(STR)
    print "".join(voteMassageCommand[0][:1])


    #-----------------------------------------------------------#
    #"when is mechanics"


    # course_names = ["infi", "mehcanics for physics students", "linear algebra"]


    #-----------------------------------------------------------------------------#
    # ---------EXPERIMENTS WITH TIME----------#

    # today = date.today()
    # #print time.hour
    # print "today is " + today
#=====================================================================================#
    print "\n THE REAL IMPORTANT TEST\n"
    print "\t    Testing class   "
    STR3 = "inFi lesson"
    st_id = 666
    myParser = Parser()
    myParser.str_parser(STR3,st_id)
    print "\n\t     Testing exam   "
    STR4 = "iNFi eXaM"
    st_id = 666
    myParser = Parser()
    myParser.str_parser(STR4,st_id)
    print "\n\t     Testing grade   "
    STR5 = "linear algebra GrAde"
    st_id = 555
    myParser = Parser()
    myParser.str_parser(STR5,st_id)
    print "\n\t     Testing vote   "
    STR6= "vote 12345 2"
    st_id = 666
    myParser = Parser()
    myParser.str_parser(STR6,st_id)
    #----------------------------------------#
    print "\n\t     Test that should fail 1  "
    STR7= "vout 12345 2"
    st_id = 666
    myParser = Parser()
    myParser.str_parser(STR7,st_id)
    print "\n\t     Test that should fail 2  "
    STR8= "INFI CLAS 2"
    st_id = 666
    myParser = Parser()
    myParser.str_parser(STR8,st_id)


    return

if __name__ == '__main__':
    main()
