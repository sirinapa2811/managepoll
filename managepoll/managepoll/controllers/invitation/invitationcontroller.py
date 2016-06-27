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


class InvitationController(TGController):
    
    allow_only = in_any_group('voter', 'managers', msg=l_('Only for people with the "manage" permission'))
    #has_any_permission('manage','creator',msg=l_('Only for people with the "manage" permission'))
    
    def __init__(self, models, session, config_type=None, translations=None):
        self.utility = Utility()
        self.model = models       
         
        
        
        
    #@require(predicates.in_any_group('creator','managers', msg=l_('Only for creator')))
    @expose('managepoll.templates.invitation.index')
    def index(self,**kw):
        user =  request.identity['user'];
        print user.user_id
                
        return dict(page = 'index',idproject = None)
        
    @expose('managepoll.templates.invitation.invitation')
    def invitation(self,**kw):
       
        print kw 
        
        
        reload(sys).setdefaultencoding("utf-8");
        invitation = self.model.Invitation()
        self.emailtemplate = self.model.EmailTemplate()
        if('idinvitation' in kw):
            print kw['idinvitation']            
            #           
            invitation = self.model.Invitation.getId(kw['idinvitation'])  
            
            
        else:
            self.emailtemplate = self.model.EmailTemplate.getTemplateBy(5); 
            
            invitation.name_content  = self.emailtemplate.sender
            invitation.from_name =  self.emailtemplate.sender
            invitation.subject =  self.emailtemplate.subject
            invitation.content =  self.emailtemplate.content_template
         
        return dict(page='invitation', invitation = invitation,idproject = None)
       
    @expose()
    def saveinvitation(self,**kw):
        user =  request.identity['user'];
        reload(sys).setdefaultencoding('utf8') 
      
        
        invitation = self.model.Invitation(**kw)
        invitation.user_id = user.user_id
        
                
        invitation.id_question_invitation = self.utility.setIfEmpty(invitation.id_question_invitation)  
        
        if self.utility.isEmpty(invitation.id_question_invitation) :    
            print "save"
            invitation.save()
        else :
            print "update"
            invitation.updateall()
      
   

        redirect('/managepoll/invitation/index')
    
        