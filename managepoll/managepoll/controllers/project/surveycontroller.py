# -*- coding: utf-8 -*-
from tg import TGController 
from tg import expose, flash, require, url, lurl,validate 
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.predicates import has_permission

from managepoll import model 
from managepoll.model import DBSession

from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime



class SurveyController(TGController):
    
    allow_only = has_permission('manage',
                                msg=l_('Only for people with the "manage" permission'))
     
    def __init__(self):
        self.utility = Utility()
    
    
    @expose('managepoll.templates.project.index')
    def index(self,**kw):               
        questionprojecttype = model.QuestionProjectType.getAll(act = 1)
        return dict(page ='index',projecttype = questionprojecttype,idproject = None)   
    
    @expose()
    def savesurfver(self,**kw):
        user =  request.identity['user'];    
        print user.user_id #user_id --login

        questionproject = model.QuestionProject(**kw)

        questionproject.user_id = user.user_id
        questionproject.save()
        
        print questionproject.id_question_project
        print questionproject.name
        print questionproject.description

        redirect('/managepoll/project/managesurfvey',params={'idproject':questionproject.id_question_project})
        
       
        
    @expose()
    def deletesurfvey(self,**kw):
        print 'Delete : Project ID :', kw['idproject']
        model.QuestionProject.deleteById(kw['idproject'])
        redirect('/surfvey')
        
    
   
    
    
    @expose('managepoll.templates.project.managesurfvey')
    def managesurfvey(self,**kw):
        print '......................'
        print kw
        
        questionproject = model.QuestionProject()
        
        if('idproject' in kw):
            print kw['idproject']
            questionproject = model.QuestionProject.getId(kw['idproject'])
        else :
            print "don't have kw"    
        #g = model.QuestionProjectType.getAll(act = 1)
        questionType = model.QuestionType.getAll(act = 1)
        return dict(page ='managesurfvey', questionproject = questionproject,questionType = questionType,idproject = kw['idproject'])
    