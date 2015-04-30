# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('sms',
                Field('num', 'string'),
                Field('body', 'text')
)

db.define_table('course',
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

db.define_table('student',
    Field('phone', 'string')
)

db.define_table('hall',
    Field('ha_id', 'integer'),
    Field('name','string')
)

db.define_table('exam',
    Field('co_id', db.course),
    Field('edate', 'string'),
    Field('ehour', 'string' ),
    Field('ha_id', db.hall),
    Field('moed', 'integer')
)

db.define_table('hgroup',
    Field('gr_id', 'integer'),
    Field('co_id', db.course),
    Field('lesson', 'string'),
)


db.define_table('studentCourse',
    Field('aid', 'integer'),
    Field('g_id','integer')
)
# For Now:
#---------------

db.hgroup.bulk_insert([{'gr_id':'8268511', 'co_id':'1070', 'lesson':'שות'},{'gr_id':'8268512', 'co_id':'1075', 'lesson':'שות'},{'gr_id':'8268513', 'co_id':'1083', 'lesson':'שות'},{'gr_id':'8268514', 'co_id':'1084', 'lesson':'שות'},{'gr_id':'8268515', 'co_id':'1100', 'lesson':'שות'}])
#
#db.student.bulk_insert([{'phone':'+9720546384009'},{'phone':'+972528899222'},{'phone':'+972547314447'}])
db.exam.bulk_insert([{'co_id':'1043','edate':'10/10/15','ehour': '13:00','ha_id':'30', 'moed':'1'}, {'co_id':'1044','edate':'10/10/15','ehour': '16:00','ha_id':'31', 'moed':'1'}, {'co_id':'1061','edate':'10/10/15','ehour': '16:00','ha_id':'32', 'moed':'1'}, {'co_id':'1065','edate':'10/10/15','ehour': '13:00','ha_id':'33', 'moed':'1'}, {'co_id':'1065','edate':'10/10/15','ehour': '16:00','ha_id':'34', 'moed':'1'}, {'co_id':'1066','edate':'10/10/15','ehour': '16:00','ha_id':'35', 'moed':'1'}, {'co_id':'1070','edate':'10/10/15','ehour': '13:00','ha_id':'35', 'moed':'1'}] )


#myset = db(db.hgroup.co_id == 	1070)
#myset.select()
#myset.update(gr_id = 8268511)
#


#-----------
db.studentCourse.bulk_insert([{'aid':'1', 'g_id':'8268511'},{'aid':'2', 'g_id':'8268512'},{'aid':'3', 'g_id':'8268513'},{'aid':'1', 'g_id':'8268514'},{'aid':'2', 'g_id':'8268515'}])
## after defining tables, uncomment below to enable auditing
auth.enable_record_versioning(db)
