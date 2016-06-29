# -*- coding: utf-8 -*-
from tg import TGController 
from tg import expose, flash, require, url, lurl,validate 
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.predicates import has_any_permission, in_any_group

#from managepoll import model 
#from managepoll.model import DBSession

from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime



class ProjectController(TGController):
    
    allow_only = in_any_group('voter', 'managers', msg=l_('Only for people with the "manage" permission'))
    
     
    def __init__(self, models, session, config_type=None, translations=None):
        super(ProjectController, self).__init__()
        
        self.model= models
        self.utility = Utility()        
    
    @expose('managepoll.templates.project.index')
    def index(self,**kw):                       
        questionprojecttype = self.model.QuestionProjectType.getAll(1)        
        return dict(page ='index',projecttype = questionprojecttype,idproject = None)   
    
    
    @expose()
    def saveproject(self,**kw):
        user =  request.identity['user'];           

        questionproject = self.model.QuestionProject(**kw)
        questionproject.user_id = user.user_id
        questionproject.save()     

        redirect('/managepoll/project/edit',params={'idproject':questionproject.id_question_project})        
       
        
    @expose()
    def delete(self,**kw):
        print 'Delete : Project ID :', kw['idproject']
        self.models.QuestionProject.deleteById(kw['idproject'])
        redirect('/index')
        
        
    @expose('managepoll.templates.project.manageproject')
    def edit(self,**kw):
        print '......................'
        print kw
        
        questionproject = self.model.QuestionProject()
        
        if('idproject' in kw):           
            questionproject = self.model.QuestionProject.getId(kw['idproject'])
        else :
            print "don't have kw"    
        #g = model.QuestionProjectType.getAll(act = 1)
        questionType = self.model.QuestionType.getAll(act = 1)
        return dict(page ='edit', questionproject = questionproject,questionType = questionType,idproject = kw['idproject'])
   
    