# -*- coding: utf-8 -*-
from gluon import current
from gluon.dal import DAL, Field
from gluon.sqlhtml import SQLFORM



class Contact(object):

    def __init__(self):
        self.db = DAL("sqlite://storage.db")
        self.session = current.session
        self.request = current.request
        self.response = current.response
        self.cache = current.cache
        self.define_table()
        #self.insert_tables()

    def define_table(self):
        self.sms = self.db.define_table('sms',
            Field('num', 'string'),
            Field('body', 'text')
        )

        self.course = self.db.define_table('course',
            Field('co_id', 'integer'),
            Field('name', 'string'),
            Field('name_eng', 'string'),
            Field('semseter', 'string'),
            Field('hug', 'string'),
            Field('lesson', 'string'),
            Field('points', 'string'),
            Field('hours', 'string'),
            Field('exam_type', 'string'),
            Field('var', 'string')
            )

        self.student = self.db.define_table('student',
            Field('phone', 'string')
            )

        self.hall = self.db.define_table('hall',
            Field('ha_id', 'integer'),
            Field('name','string')
            )

        self.exam = self.db.define_table('exam',
            Field('co_id', self.db.course),
            Field('edate', 'string'),
            Field('ehour', 'string' ),
            Field('ha_id', self.db.hall),
            Field('moed', 'integer')
            )

        self.hgroup = self.db.define_table('hgroup',
            Field('gr_id', 'integer'),
            Field('co_id', self.db.course),
            Field('lesson', 'string'),
            )


        self.studentCourse = self.db.define_table('studentCourse',
            Field('aid', 'integer'),
            Field('g_id','integer')
            )
         #def insert_tables(self):
        self.db.course.bulk_insert([{'co_id':'1070'},{'co_id':'1075'},{'co_id':'1083'},{'co_id':'1100'},{'co_id':'1084'}])
        #self.db.hgroup.bulk_insert([{'gr_id':'8268511', 'co_id':'1070', 'lesson':'שות'},{'gr_id':'8268512', 'co_id':'1075', 'lesson':'שות'},{'gr_id':'8268513', 'co_id':'1083', 'lesson':'שות'},{'gr_id':'8268514', 'co_id':'1084', 'lesson':'שות'},{'gr_id':'8268515', 'co_id':'1100', 'lesson':'שות'}])
        #self.db.exam.bulk_insert([{'co_id':'1043','edate':'10/10/15','ehour': '13:00','ha_id':'30', 'moed':'1'}, {'co_id':'1044','edate':'10/10/15','ehour': '16:00','ha_id':'31', 'moed':'1'}, {'co_id':'1061','edate':'10/10/15','ehour': '16:00','ha_id':'32', 'moed':'1'}, {'co_id':'1065','edate':'10/10/15','ehour': '13:00','ha_id':'33', 'moed':'1'}, {'co_id':'1065','edate':'10/10/15','ehour': '16:00','ha_id':'34', 'moed':'1'}, {'co_id':'1066','edate':'10/10/15','ehour': '16:00','ha_id':'35', 'moed':'1'}, {'co_id':'1070','edate':'10/10/15','ehour': '13:00','ha_id':'35', 'moed':'1'}] )
        self.db.student.bulk_insert([{'phone':'+9720546384009'},{'phone':'+972528899222'},{'phone':'+972547314447'}])
        self.db.studentCourse.bulk_insert([{'aid':'1', 'g_id':'8268511'},{'aid':'2', 'g_id':'8268512'},{'aid':'3', 'g_id':'8268513'},{'aid':'1', 'g_id':'8268514'},{'aid':'2', 'g_id':'8268515'}])
    def search_class_ta(self, sid, course_num):
        rows = self.db(self.db.student.id == sid & self.db.course.co_id==self.db.hgroup.co_id ).select()
        return rows


#


#myset = db(db.hgroup.co_id == 	1070)
#myset.select()
#myset.update(gr_id = 8268511)
#


#-----------
