__author__ = 'shaharo02'

import re

class Parser:

    #Constant words
    exam_syn = ["exam", "moed", "test"]
    TA_syn = ["tirgul", "TA"]
    lecture_syn = ["lecture", "shiur"]
    class_syn = ["class"] + TA_syn + lecture_syn

    # Parses a string relative to the given student id
    def str_parser(self, str_to_parse, st_id):

        #Search for one of the constant words
        # if matched with exam_syn -> parse_exam(str_to_parse, st_id)
        #else -> parse_class()

        str_to_parse = str.lower(str_to_parse)
        exam = re.compile("exam"|"moed"|"test")
        if exam.match(str_to_parse):
            self.parse_exam(str_to_parse, st_id)
        elif

        str_to_parse.

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

     def parse_exam(self, str_to_parse, st_id):
         pass


    def parse_class(self, str_to_parse, st_id):
         pass

