# -*- coding: utf-8 -*-

from tg import TGController 
from tg import expose, flash, require, url, lurl,validate 
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.predicates import has_any_permission, in_any_group





from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime

class LoadDataControllers(TGController):   
    allow_only = in_any_group('voter', 'managers', msg=l_('Only for people with the "manage" permission'))
    #has_any_permission('manage','creator', msg=l_('Only for people with the "manage" permission'))
    def __init__(self, models, session, config_type=None, translations=None):
        self.utility = Utility()
        self.model = models       
        
   
        
    @expose('json')
    def getdatainvittation(self,**kw):
        print "****************"
        print kw
        user =  request.identity['user'];
        values,total = self.model.Invitation.getByUser(userid=user.user_id,page=(int(kw['current'])-1), page_size=int(kw['rowCount']))              
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values) 
    
    @expose('json')
    def getdataproject(self,**kw):
        print kw        
        user =  request.identity['user'];        
        values,total = self.model.QuestionProject.getAllByUser(userid=user.user_id,page=(int(kw['current'])-1), page_size=int(kw['rowCount']))   
        print values     
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values)
    
    @expose('json')
    def getdatapublication(self,**kw):   
        values,total = self.model.QuestionOption.getByProject(idProject=kw['id'],page=(int(kw['current'])-1), page_size=int(kw['rowCount']))            
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values)
    
    @expose('json')
    def getdatavoter(self,**kw):        
        print kw        
        user =  request.identity['user'];          
        print user.user_id              
        data,total = self.model.Voter.getListVoterByOwner(user_id_owner=user.user_id,page=(int(kw['current'])-1), page_size=int(kw['rowCount']))        
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = data)
    
    