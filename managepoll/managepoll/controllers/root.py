# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController

from managepoll import model
from managepoll.model import DBSession

from tg import expose, flash, require, url, lurl, validate
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from mytemplate import model
from mytemplate.controllers.secure import SecureController
from mytemplate.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from mytemplate.lib.base import BaseController
from mytemplate.controllers.error import ErrorController
import mytemplate
from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime

class RootController(TGController):
    @expose('managepoll.templates.index')
    def index(self):
        flash(_("Hello World!"))
        pass
    
    @require(predicates.in_any_group('creator','managers', msg=l_('Only for creator')))
    @expose('managepoll.templates.surfvey')
    def surfvey(self,**kw):
               
        p = model.QuestionProjectType.getAll(act = 1)
        return dict(page ='surfvey',projecttype = p)
    
   
    @expose('json')
    def getdataproject(self,**kw):
        print kw
        
        user =  request.identity['user'];        
        values,total = model.QuestionProject.getAllByUser(userid=user.user_id,page=int(kw['current']), page_size=int(kw['rowCount']))
        
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values)
    
    @expose('managepoll.templates.managesurfvey')
    def managesurfvey(self,**kw):
        print '......................'
        print kw
        
        questionproject = model.QuestionProject()
        
        if('idproject' in kw):
            print kw['idproject']
            questionproject = model.QuestionProject.getAllByUser(kw['idproject'])
        else :
            print "don't have kw"    
        #g = model.QuestionProjectType.getAll(act = 1)
        questionType = model.QuestionType.getAll(act = 1)
        return dict(page ='managesurfvey', questionproject = questionproject,questionType = questionType)
    